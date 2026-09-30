<template>
  <div class="app-shell">
    <aside class="app-side">
      <h1 class="app-title">会展布展搭建管理平台</h1>
      <nav class="nav-list">
        <RouterLink v-for="item in navItems" :key="item.path" :to="item.path" class="nav-item">
          {{ item.label }}
        </RouterLink>
      </nav>
    </aside>
    <main class="app-main">
      <header class="app-head">
        <span class="head-desc">面向展会立项、展位分配、展位设计、搭建施工、用电申报与消防验收的一体化布展管理后台。</span>
        <span class="head-user">当前值班：{{ store.operator }} · {{ store.shiftLabel }}</span>
      </header>
      <RouterView />
    </main>
  </div>
</template>

<script setup lang="ts">
import { useSessionStore } from '@/stores/session'

const store = useSessionStore()

const navItems = [{ label: "运营概览", path: "/" }, { label: "展会立项", path: "/project" }, { label: "展位分配", path: "/booth" }, { label: "参展单位", path: "/exhibitor" }, { label: "展位设计", path: "/design" }, { label: "搭建施工", path: "/construction" }, { label: "展具租赁", path: "/material" }, { label: "用电申报", path: "/power" }, { label: "消防验收", path: "/fire" }, { label: "现场安全", path: "/safety" }, { label: "安保通行", path: "/security" }, { label: "展品运输", path: "/logistics" }, { label: "撤展清运", path: "/cleaning" }, { label: "排期计划", path: "/schedule" }, { label: "布展收费", path: "/fee" }, { label: "承建单位", path: "/contractor" }, { label: "投诉处理", path: "/complaint" }, { label: "项目结算", path: "/settlement" }, { label: "展会复盘", path: "/review" }]
</script>
