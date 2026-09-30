import { createRouter, createWebHistory } from 'vue-router'

import Dashboard from '@/views/Dashboard.vue'
const Project = () => import('@/views/project/index.vue')
const Booth = () => import('@/views/booth/index.vue')
const Exhibitor = () => import('@/views/exhibitor/index.vue')
const Design = () => import('@/views/design/index.vue')
const Construction = () => import('@/views/construction/index.vue')
const Material = () => import('@/views/material/index.vue')
const Power = () => import('@/views/power/index.vue')
const Fire = () => import('@/views/fire/index.vue')
const Safety = () => import('@/views/safety/index.vue')
const Security = () => import('@/views/security/index.vue')
const Logistics = () => import('@/views/logistics/index.vue')
const Cleaning = () => import('@/views/cleaning/index.vue')
const Schedule = () => import('@/views/schedule/index.vue')
const Fee = () => import('@/views/fee/index.vue')
const Contractor = () => import('@/views/contractor/index.vue')
const Complaint = () => import('@/views/complaint/index.vue')
const Settlement = () => import('@/views/settlement/index.vue')
const Review = () => import('@/views/review/index.vue')

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'dashboard', component: Dashboard },
    { path: '/project', name: 'project', component: Project },
    { path: '/booth', name: 'booth', component: Booth },
    { path: '/exhibitor', name: 'exhibitor', component: Exhibitor },
    { path: '/design', name: 'design', component: Design },
    { path: '/construction', name: 'construction', component: Construction },
    { path: '/material', name: 'material', component: Material },
    { path: '/power', name: 'power', component: Power },
    { path: '/fire', name: 'fire', component: Fire },
    { path: '/safety', name: 'safety', component: Safety },
    { path: '/security', name: 'security', component: Security },
    { path: '/logistics', name: 'logistics', component: Logistics },
    { path: '/cleaning', name: 'cleaning', component: Cleaning },
    { path: '/schedule', name: 'schedule', component: Schedule },
    { path: '/fee', name: 'fee', component: Fee },
    { path: '/contractor', name: 'contractor', component: Contractor },
    { path: '/complaint', name: 'complaint', component: Complaint },
    { path: '/settlement', name: 'settlement', component: Settlement },
    { path: '/review', name: 'review', component: Review },
  ],
})

export default router
