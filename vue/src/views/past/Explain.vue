<template>

  <div>
    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item title="1.界面说明" name="1">
        <el-card class="box-card" shadow="hover">
          <el-collapse-item title="a.侧边栏" name="1.1">
            <el-card class="box-card" >
              <div>·侧边栏中具有以下五点内容：主页、信息查询、如有疑问？、系统恢复与备份；</div>
              <div>·其中信息查询中包括：用户信息、停车场信息、订单信息的子功能；</div>
              <div>·其中如有疑问中包括：说明文档和联系我们的子功能</div>
            </el-card>

          </el-collapse-item>

          <el-collapse-item title="b.导航栏" name="1.2">
            <el-card class="box-card" >
              <div>·导航栏在侧边栏最上方的右侧，具有显示当前界面位置的功能；</div>
              <div>·如：现在在首页/说明文档的位置，因此我们的导航栏显示这样的文字；</div>
            </el-card>

          </el-collapse-item>

          <el-collapse-item title="c.用户图标" name="1.4">
            <el-card class="box-card" >
              <div>·用户图标在右上角的位置，具有查看个人信息和退出界面的功能，将鼠标放置到图标位置处即可展开菜单栏；</div>
              <div>·点击个人信息可以跳转到个人信息界面；</div>
              <div>·点击退出登录可以跳转到登录注册界面；</div>
            </el-card>

          </el-collapse-item>

          <el-collapse-item title="d.主要界面" name="1.3">
            <el-card class="box-card" >
              <div>·主要界面处于页面的中心位置，用户显示相关功能的信息和操作功能；</div>
            </el-card>

          </el-collapse-item>

        </el-card>



      </el-collapse-item>

      <el-collapse-item title="2.业务说明" name="2">
        <el-card class="box-card" >本系统用于对停车管理员管理用户信息、停车场信息、订单信息以及系统相关备份恢复的数字化实现，所以存在许多相关问题须待改进。</el-card>
      </el-collapse-item>

      <el-collapse-item title="3.免责声明" name="3">
        <el-card class="box-card" >本系统仅为上海工程技术大学软工实验设计课程的作业，可以仅供学习参考使用，如实际运用造成任何问题概不负责！</el-card>
      </el-collapse-item>
      <el-collapse-item title="4.其他" name="4">
        <el-card class="box-card" >
        <div>本系统开发非常简易，许多功能并不可靠，如有问题可以邮件联系告知。</div>
        <div>QQ邮箱：1595916384@qq.com</div>
        </el-card>
      </el-collapse-item>
    </el-collapse>

  </div>


</template>

<script>
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Explain"
}
</script>

<style scoped>

</style>
<script>
export default {
  data() {
    return {
      activeNames: ['']
    };
  },
  methods: {
    handleChange(val) {
      console.log(val);
    }
  }
}
</script>