import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from "core-js/internals/shared-store";
import store from "@/store";

Vue.use(VueRouter)

const routes = [



  {
    path: '/login',
    name: 'Login',
    component: () => import( '../views/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import( '../views/Register.vue')
  },

  {
    path: '/',
    name: 'Manage',
    component: ()=>import('../views/Manage.vue'),
    redirect:"/home",
    children:[
      {path: 'home', name: '', component: ()=>import('../views/Home.vue')},
      {path: 'user', name: '用户管理', component: ()=>import('../views/User.vue')},
      {path: 'person', name: '个人信息', component: ()=>import('../views/Person.vue')},
      {path: 'ParkingLot', name: '停车场信息', component: ()=>import('../views/ParkingLot.vue')},
      {path: 'Explain', name: '说明文档', component: () => import( '../views/Explain.vue')},
      {path: 'Linkus', name: '联系我们', component: () => import( '../views/Linkus.vue')},
      {path: 'Order', name: '订单信息', component: () => import( '../views/Order.vue')},
      {path: 'ParkingSpace', name: '停车位信息', component: () => import( '../views/ParkingSpace.vue')},
      {path: 'Echart_user', name: '用户注册趋势', component: () => import( '../views/Echart_user.vue')},
      {path: 'Echart_park', name: '停车场数量可视化', component: () => import( '../views/Echart_park.vue')},
      {path: 'time_ui', name: '时间', component: () => import( '../views/time_ui.vue')},
      {path: 'gdmap', name: '高德地图', component: () => import( '../views/gdmap.vue')},
      {path: 'bookspace', name: '预定停车位', component: () => import( '../views/BookSpace.vue')},
      {path: 'park', name: '停车', component: () => import( '../views/Park.vue')},
      {path: 'rules', name: '关联规则', component: () => import( '../views/DA/rules.vue')},
      {path: 'cluster', name: '聚类分析', component: () => import( '../views/DA/cluster')},
      {path: 'classify', name: '分类分析', component: () => import( '../views/DA/classify')},
      {path: 'regression', name: '回归分析', component: () => import( '../views/DA/regression')},
    ],
  },
  {
    path: '/about',
    name: 'about',
    component: () => import( '../views/AboutView.vue')
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  localStorage.setItem("currentPathName", to.name)  // 设置当前的路由名称，为了在Header组件中去使用
  store.commit("setPath")  // 触发store的数据更新
  next()  // 放行路由
})

export default router
