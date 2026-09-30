<template>
  <section class="page">
    <header class="page-head">
      <div>
        <h2>运营概览</h2>
        <p class="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
      </div>
    </header>
    <div class="stat-row">
      <article v-for="card in cards" :key="card.label" class="stat-card">
        <span class="stat-label">{{ card.label }}</span>
        <strong class="stat-value">{{ card.value }}</strong>
      </article>
    </div>
    <table class="data-table">
      <thead>
        <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
      </thead>
      <tbody>
        <tr v-for="row in moduleRows" :key="row.name">
          <td>{{ row.name }}</td>
          <td>{{ row.created }}</td>
          <td>{{ row.pending }}</td>
          <td>{{ row.abnormal }}</td>
        </tr>
      </tbody>
    </table>
  </section>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const cards = ref<Overview['cards']>([])
const moduleRows = ref<Overview['modules']>([])

onMounted(async () => {
  try {
    const payload = await fetchJson<Overview>('/api/overview')
    cards.value = payload.cards
    moduleRows.value = payload.modules
  } catch {
    cards.value = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
    moduleRows.value = [{"name": "展会立项", "created": 0, "pending": 0, "abnormal": 0}, {"name": "展位分配", "created": 0, "pending": 0, "abnormal": 0}, {"name": "参展单位", "created": 0, "pending": 0, "abnormal": 0}, {"name": "展位设计", "created": 0, "pending": 0, "abnormal": 0}, {"name": "搭建施工", "created": 0, "pending": 0, "abnormal": 0}, {"name": "展具租赁", "created": 0, "pending": 0, "abnormal": 0}, {"name": "用电申报", "created": 0, "pending": 0, "abnormal": 0}, {"name": "消防验收", "created": 0, "pending": 0, "abnormal": 0}, {"name": "现场安全", "created": 0, "pending": 0, "abnormal": 0}, {"name": "安保通行", "created": 0, "pending": 0, "abnormal": 0}, {"name": "展品运输", "created": 0, "pending": 0, "abnormal": 0}, {"name": "撤展清运", "created": 0, "pending": 0, "abnormal": 0}, {"name": "排期计划", "created": 0, "pending": 0, "abnormal": 0}, {"name": "布展收费", "created": 0, "pending": 0, "abnormal": 0}, {"name": "承建单位", "created": 0, "pending": 0, "abnormal": 0}, {"name": "投诉处理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "项目结算", "created": 0, "pending": 0, "abnormal": 0}, {"name": "展会复盘", "created": 0, "pending": 0, "abnormal": 0}]
  }
})
</script>
