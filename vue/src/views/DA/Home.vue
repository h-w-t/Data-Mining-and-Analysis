<template>
  <div class="text-container">
    <h1 class="animated-text">{{ text }}</h1>
  </div>
</template>

<script>
import Home from "@/views/DA/Home";

export default {
  name:Home,
  data() {
    return {
      text: '欢迎使用大数据可视化分析系统',
      colors: ['#FFC107', '#FF5722', '#8BC34A', '#03A9F4'], // 渐变色列表
      currentIndex: 0, // 当前颜色索引
    };
  },
  mounted() {
    this.animateText();//this.animateText() 方法用于启动文字的动画效果
  },
  methods: {
    animateText() {
      setInterval(() => {
        this.currentIndex = (this.currentIndex + 1) % this.colors.length;
      }, 1000); // 每秒切换颜色，可根据需要调整时间间隔
    },
  },
  computed: {
    currentColor() {
      return this.colors[this.currentIndex];
    },
  },
};
</script>

<style>
.text-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.animated-text {
  font-size: 24px;
  text-align: center;
  margin-top: -20px; /* 根据需要调整文字向上的偏移量 */
  animation: gradientAnimation 5s infinite;
}

@keyframes gradientAnimation {
  0% {
    color: #FFC107;
  }
  25% {
    color: #FF5722;
  }
  50% {
    color: #8BC34A;
  }
  75% {
    color: #03A9F4;
  }
  100% {
    color: #FFC107;
  }
}
</style>
