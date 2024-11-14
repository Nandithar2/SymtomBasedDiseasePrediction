import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import History from '../components/History.vue';
import Settings from '../components/Settings.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/history', component: History },
  { path: '/settings', component: Settings }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
