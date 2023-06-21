<template>
  <div id="container"></div>
</template>

<script>
import AMapLoader from '@amap/amap-jsapi-loader';

export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "gdmap",
  data() {
    return {
      map: null,
      markers: [
        {
          position: [121.206283,31.055301],
          info: {
            name: '工技大松江停车场',
            address: '上海市松江区龙腾路333号',
            capacity: 500,
            manager: 'Tom',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
        {
          position: [121.213164,31.055582],
          info: {
            name: '东华松江停车场',
            address: '上海市松江区人民北路2999号',
            capacity: 700,
            manager: 'Tom',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
        {
          position: [121.436882,31.025626],
          info: {
            name: '交大闵行停车场',
            address: '上海市闵行区东川路800号',
            capacity: 900,
            manager: 'Giles',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
        {
          position: [121.396831,31.204758],
          info: {
            name: '工技大长宁停车场',
            address: '上海市长宁区仙霞路350号',
            capacity: 200,
            manager: 'Tom',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
        {
          position: [121.41494,31.204408],
          info: {
            name: '东华长宁停车场',
            address: '上海市长宁区延安西路1882号',
            capacity: 700,
            manager: 'Tom',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
        {
          position: [121.433116,31.198981],
          info: {
            name: '交大徐汇停车场',
            address: '上海市徐汇区华山路1954号',
            capacity: 750,
            manager: 'Tom',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
        {
          position: [121.555588,31.291341],
          info: {
            name: '上理杨浦停车场',
            address: '上海市杨浦区军工路516号',
            capacity: 700,
            manager: 'Tom',
            contact: '13761056216',
          },
          infoWindowOpen: false,
        },
      ],
      infoWindow: null,
      lastClickedMarker: null,
    };
  },
  methods: {
    initMap() {
      AMapLoader.load({
        key: "64444c7c6c39b70246970756e86474b0",
        version: "2.0",
        plugins: [],
      }).then((AMap) => {
        this.map = new AMap.Map("container", {
          viewMode: "3D",
          zoom: 18,
          center: [121.206283, 31.055301],
        });

        // 创建自定义信息窗体
        this.infoWindow = new AMap.InfoWindow({
          isCustom: true,
          offset: new AMap.Pixel(0, -30),
          closeWhenClickMap: true, // 点击地图关闭信息窗体
          showShadow: true, // 显示信息窗体阴影
        });

        // 在地图上添加点坐标信息
        this.markers.forEach((markerInfo) => {
          const marker = new AMap.Marker({
            position: markerInfo.position,
          });

          // 添加事件监听器，点击时显示/关闭信息窗体
          marker.on("click", () => {
            if (this.lastClickedMarker === marker) {
              // 关闭已点击的标记点
              this.closeInfoWindow();
            } else {
              // 显示新的标记点
              this.showInfoWindow(markerInfo.position, markerInfo.info);
              this.lastClickedMarker = marker;
            }
          });

          // 添加事件监听器，鼠标移入显示信息窗体
          marker.on("mouseover", () => {
            if (this.lastClickedMarker !== marker) {
              this.showInfoWindow(markerInfo.position, markerInfo.info);
            }
          });

          // 添加事件监听器，鼠标移出关闭信息窗体
          marker.on("mouseout", () => {
            if (this.lastClickedMarker !== marker) {
              this.closeInfoWindow();
            }
          });

          this.map.add(marker);
        });
      }).catch((error) => {
        console.log(error);
      });
    },
    showInfoWindow(position, info) {
      const content = `
        <div class="info-window">
          <div class="info-window-header">停车场信息</div>
          <div class="info-window-content">
            <p><b>停车场名：</b>${info.name}</p>
            <p><b>地址：</b>${info.address}</p>
            <p><b>车位数量：</b>${info.capacity}</p>
            <p><b>管理员：</b>${info.manager}</p>
            <p><b>联系方式：</b>${info.contact}</p>
          </div>
        </div>
      `;

      this.infoWindow.setContent(content);
      this.infoWindow.open(this.map, position);
    },
    closeInfoWindow() {
      this.infoWindow.close();
      this.lastClickedMarker = null;
    },
  },
  mounted() {
    this.initMap();
  },
};
</script>

<style scoped>
#container {
  padding: 0px;
  margin: 0px;
  width: 100%;
  height: 90vh;
}

.info-window {
  padding: 10px;
  background-color: #fff;
  border-radius: 4px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.3);
  font-size: 14px;
}

.info-window-header {
  font-weight: bold;
  margin-bottom: 5px;
}

.info-window-content {
  line-height: 1.5;
}
</style>
