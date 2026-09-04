<script setup lang="ts">
import { computed, ref } from 'vue'
import catalog from '../../../src/data/generated/catalog.json'

type Localized = Record<string, string>
type Resource = {
  id: string
  channel: string
  name: Localized
  description: Localized
  categories: string[]
  tags: string[]
  status: 'active' | 'review' | 'deprecated'
  lastVerifiedAt: string
  website: string
  detailPath: string
}

const props = defineProps<{ channel?: string }>()
const pageSize = 6
const query = ref('')
const category = ref('')
const sort = ref<'updated' | 'name'>('updated')
const page = ref(1)

const channelMeta: Record<string, { title: string; description: string }> = {
  mcp: { title: 'MCP 服务', description: '可导入 ChatSpeed 的 MCP 服务目录' },
  models: { title: '模型供应商', description: '适用于 ChatSpeed 的模型供应商与推理接口' },
  'free-ai': { title: '免费 AI', description: '免费 AI 网站与 API 服务目录，额度以官方信息为准' }
}
const channelLinks = [
  { id: 'mcp', label: 'MCP 服务', icon: 'M' },
  { id: 'models', label: '模型供应商', icon: 'A' },
  { id: 'free-ai', label: '免费 AI', icon: 'F' }
]
const statusLabels = { active: '已验证', review: '待复核', deprecated: '已弃用' }

const allItems = computed(() => catalog.items as Resource[])
const sourceItems = computed(() => props.channel ? allItems.value.filter(item => item.channel === props.channel) : [...allItems.value])
const meta = computed(() => channelMeta[props.channel || ''] || { title: '资源中心', description: 'ChatSpeed 生态资源目录' })
const categories = computed(() => {
  const counts = new Map<string, number>()
  sourceItems.value.forEach(item => item.categories.forEach(value => counts.set(value, (counts.get(value) || 0) + 1)))
  return [...counts.entries()].sort((a, b) => a[0].localeCompare(b[0]))
})
const filteredItems = computed(() => {
  const search = query.value.trim().toLowerCase()
  return sourceItems.value
    .filter(item => !search || [item.name.zh-Hans, item.name.en, item.description.zh-Hans, ...item.categories, ...item.tags].join(' ').toLowerCase().includes(search))
    .filter(item => !category.value || item.categories.includes(category.value))
    .sort((a, b) => sort.value === 'name' ? text(a.name).localeCompare(text(b.name)) : b.lastVerifiedAt.localeCompare(a.lastVerifiedAt))
})
const pageCount = computed(() => Math.max(1, Math.ceil(filteredItems.value.length / pageSize)))
const visibleItems = computed(() => filteredItems.value.slice((page.value - 1) * pageSize, page.value * pageSize))

// Windowed pager: at most 7 numbered buttons = 3 before + current + 3 after, clamped to [1, pageCount].
const pageWindow = computed(() => {
  const total = pageCount.value
  const size = 7
  const current = Math.min(Math.max(1, page.value), total)
  let start = Math.max(1, current - 3)
  const end = Math.min(total, start + size - 1)
  start = Math.max(1, end - size + 1)
  return Array.from({ length: end - start + 1 }, (_, i) => start + i)
})
const goPage = (n: number) => { page.value = Math.min(Math.max(1, n), pageCount.value) }

const text = (values: Localized) => values['zh-Hans'] || values.en || Object.values(values)[0] || ''
const channelName = (id: string) => channelMeta[id]?.title || id
const resetPage = () => { page.value = 1 }
const setCategory = (value: string) => { category.value = value; resetPage() }
const initials = (name: string) => name.split(/\s+/).map(part => part[0]).join('').slice(0, 2).toUpperCase()
</script>

<template>
  <main class="resource-shell">
    <section class="resource-heading">
      <div>
        <p class="eyebrow">CHATSPEED RESOURCE CENTER</p>
        <h1>{{ meta.title }}</h1>
        <p>{{ meta.description }}</p>
      </div>
      <a class="submit-link" href="https://github.com/aidyou/chatspeed-res" target="_blank" rel="noopener">提交资源 <span>↗</span></a>
    </section>

    <div class="resource-layout">
      <aside class="resource-sidebar" aria-label="资源频道和分类">
        <div class="sidebar-section">
          <p class="sidebar-title">资源频道</p>
          <a v-for="link in channelLinks" :key="link.id" class="channel-link" :class="{ active: link.id === props.channel }" :href="`/${link.id}/`">
            <span class="channel-icon">{{ link.icon }}</span><span>{{ link.label }}</span><strong>{{ allItems.filter(item => item.channel === link.id).length }}</strong>
          </a>
          <a class="channel-link" :class="{ active: !props.channel }" href="/"><span class="channel-icon">✦</span><span>全部资源</span><strong>{{ allItems.length }}</strong></a>
        </div>
        <div v-if="props.channel" class="sidebar-section category-section">
          <p class="sidebar-title">当前分类</p>
          <button class="category-link" :class="{ active: !category }" @click="setCategory('')"><span>全部 {{ meta.title }}</span><strong>{{ sourceItems.length }}</strong></button>
          <button v-for="[name, count] in categories" :key="name" class="category-link" :class="{ active: category === name }" @click="setCategory(name)"><span>{{ name }}</span><strong>{{ count }}</strong></button>
        </div>
        <div class="sidebar-section sidebar-help">
          <p class="sidebar-title">相关链接</p>
          <a href="/guide/">使用说明 <span>→</span></a>
          <a href="https://aidyou.ai" target="_blank" rel="noopener">ChatSpeed 官网 <span>↗</span></a>
        </div>
      </aside>

      <section class="resource-content" aria-label="资源列表">
        <div class="content-toolbar">
          <div><h2>{{ meta.title }}资源</h2><span>共 {{ filteredItems.length }} 个资源</span></div>
          <label class="search-box"><span aria-hidden="true">⌕</span><input v-model="query" @input="resetPage" type="search" :placeholder="`搜索${meta.title}、标签或关键词`" :aria-label="`搜索${meta.title}`" /></label>
        </div>
        <div class="filter-row">
          <span class="filter-label">筛选：</span>
          <button class="filter-chip" :class="{ selected: !category }" @click="setCategory('')">全部标签</button>
          <button v-for="[name] in categories.slice(0, 5)" :key="name" class="filter-chip" :class="{ selected: category === name }" @click="setCategory(name)">{{ name }}</button>
          <label class="sort-select">排序：<select v-model="sort" @change="resetPage"><option value="updated">最近更新</option><option value="name">名称</option></select></label>
        </div>

        <div v-if="visibleItems.length" class="resource-list">
          <a v-for="item in visibleItems" :key="item.id" class="resource-card" :href="`/${item.channel}/${item.id}.html`">
            <div class="card-top"><span class="resource-avatar">{{ initials(text(item.name)) }}</span><div class="card-title"><h3>{{ text(item.name) }}</h3><span class="status" :class="`status-${item.status}`">{{ statusLabels[item.status] }}</span></div><span class="card-arrow">→</span></div>
            <p class="card-description">{{ text(item.description) }}</p>
            <div class="card-tags"><span v-for="tag in item.tags.slice(0, 4)" :key="tag">{{ tag }}</span></div>
            <div class="card-meta"><span>{{ channelName(item.channel) }}</span><span>最近验证：{{ item.lastVerifiedAt }}</span></div>
          </a>
        </div>
        <div v-else class="empty-state"><strong>没有找到匹配资源</strong><span>试试其他关键词或清除筛选条件。</span><button @click="query = ''; setCategory('')">清除筛选</button></div>

        <nav v-if="pageCount > 1" class="pagination" aria-label="资源分页">
          <button v-if="page > 1" @click="goPage(1)">首页</button>
          <button v-if="page > 1" @click="goPage(page - 1)">上一页</button>
          <button v-for="number in pageWindow" :key="number" :class="{ current: page === number }" :aria-current="page === number ? 'page' : undefined" @click="goPage(number)">{{ number }}</button>
          <button v-if="page < pageCount" @click="goPage(page + 1)">下一页</button>
          <button v-if="page < pageCount" @click="goPage(pageCount)">尾页</button>
        </nav>
      </section>
    </div>
  </main>
</template>
