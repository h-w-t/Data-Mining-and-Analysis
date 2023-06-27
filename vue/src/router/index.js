import Vue from 'vue'
import VueRouter from 'vue-router'
// import store from "core-js/internals/shared-store";
import store from "@/store";

Vue.use(VueRouter)

const routes = [



  {
    path: '/login',
    name: 'Login',
    component: () => import( '../views/DA/Login.vue')
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import( '../views/DA/Register.vue')
  },

  {
    path: '/',
    name: 'Manage',
    component: ()=>import('../views/DA/Manage.vue'),
    redirect:"/home",
    children:[
      {path: 'home', name: '', component: ()=>import('../views/DA/Home.vue')},
      {path: 'rules', name: '关联规则', component: () => import( '../views/DA/rules.vue')},
      {path: 'cluster', name: '聚类分析', component: () => import( '../views/DA/cluster')},
      {path: 'classify', name: '分类分析', component: () => import( '../views/DA/classify')},
      {path: 'regression', name: '回归分析', component: () => import( '../views/DA/regression')},
    ],
  },
  {
    path: '/about',
    name: 'about',
    component: () => import( '../views/DA/AboutView.vue')
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
