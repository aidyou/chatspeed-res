<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute } from 'vuepress/client'
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
const route = useRoute()
const pageSize = 10
const query = ref('')
const category = ref('')
const sort = ref<'updated' | 'name'>('updated')
const page = ref(1)

// Locale is derived from the route path: everything under /zh/ is Chinese, the
// rest of the site is the English default. The same component serves both.
const isZh = computed(() => route.path === '/zh' || route.path.startsWith('/zh/'))
const locale = computed(() => (isZh.value ? 'zh-Hans' : 'en'))
const prefix = computed(() => (isZh.value ? '/zh' : ''))

const UI: Record<string, any> = {
  en: {
    submit: 'Submit a resource',
    channels: 'Channels',
    allResources: 'All resources',
    categories: 'Categories',
    all: 'All',
    related: 'Related links',
    guide: 'Guide',
    site: 'ChatSpeed site',
    filter: 'Filter:',
    allTags: 'All tags',
    sort: 'Sort:',
    sortUpdated: 'Recently updated',
    sortName: 'Name',
    verified: 'Verified: ',
    emptyTitle: 'No matching resources',
    emptyHint: 'Try other keywords or clear your filters.',
    emptyClear: 'Clear filters',
    first: 'First', prev: 'Prev', next: 'Next', last: 'Last',
    ariaChannels: 'Channels and categories',
    ariaList: 'Resource list',
    ariaPager: 'Pagination',
    contentTitle: (title: string) => title,
    count: (n: number) => `${n} resources`,
    search: (title: string) => `Search ${title}, tags or keywords`,
    searchAria: (title: string) => `Search ${title}`,
  },
  'zh-Hans': {
    submit: '提交资源',
    channels: '资源频道',
    allResources: '全部资源',
    categories: '当前分类',
    all: '全部',
    related: '相关链接',
    guide: '使用说明',
    site: 'ChatSpeed 官网',
    filter: '筛选：',
    allTags: '全部标签',
    sort: '排序：',
    sortUpdated: '最近更新',
    sortName: '名称',
    verified: '最近验证：',
    emptyTitle: '没有找到匹配资源',
    emptyHint: '试试其他关键词或清除筛选条件。',
    emptyClear: '清除筛选',
    first: '首页', prev: '上一页', next: '下一页', last: '尾页',
    ariaChannels: '资源频道和分类',
    ariaList: '资源列表',
    ariaPager: '资源分页',
    contentTitle: (title: string) => `${title}资源`,
    count: (n: number) => `共 ${n} 个资源`,
    search: (title: string) => `搜索${title}、标签或关键词`,
    searchAria: (title: string) => `搜索${title}`,
  },
}
const t = computed(() => UI[locale.value])

const channelMeta: Record<string, Record<string, { title: string; description: string }>> = {
  en: {
    mcp: { title: 'MCP Servers', description: 'MCP servers you can import into ChatSpeed' },
    'free-ai': { title: 'Free AI', description: 'Free AI services; entries with a provider config import into ChatSpeed' },
    home: { title: 'Resource Center', description: 'ChatSpeed ecosystem resource catalog' },
  },
  'zh-Hans': {
    mcp: { title: 'MCP 服务', description: '可导入 ChatSpeed 的 MCP 服务目录' },
    'free-ai': { title: '免费 AI', description: '免费 AI 服务目录；自带供应商配置的服务可直接导入 ChatSpeed' },
    home: { title: '资源中心', description: 'ChatSpeed 生态资源目录' },
  },
}
const channelLinks: Record<string, { id: string; label: string; icon: string }[]> = {
  en: [
    { id: 'mcp', label: 'MCP Servers', icon: 'M' },
    { id: 'free-ai', label: 'Free AI', icon: 'F' },
  ],
  'zh-Hans': [
    { id: 'mcp', label: 'MCP 服务', icon: 'M' },
    { id: 'free-ai', label: '免费 AI', icon: 'F' },
  ],
}
const statusLabels: Record<string, Record<string, string>> = {
  en: { active: 'Verified', review: 'In review', deprecated: 'Deprecated' },
  'zh-Hans': { active: '已验证', review: '待复核', deprecated: '已弃用' },
}

const allItems = computed(() => catalog.items as Resource[])
const sourceItems = computed(() => (props.channel ? allItems.value.filter(item => item.channel === props.channel) : [...allItems.value]))
const meta = computed(() => channelMeta[locale.value][props.channel || 'home'] || channelMeta[locale.value].home)
const links = computed(() => channelLinks[locale.value])
const statuses = computed(() => statusLabels[locale.value])
const categories = computed(() => {
  const counts = new Map<string, number>()
  sourceItems.value.forEach(item => item.categories.forEach(value => counts.set(value, (counts.get(value) || 0) + 1)))
  return [...counts.entries()].sort((a, b) => a[0].localeCompare(b[0]))
})
// Match across every localized name/description value plus categories and tags.
const searchHaystack = (item: Resource) =>
  [...Object.values(item.name), ...Object.values(item.description), ...item.categories, ...item.tags].join(' ').toLowerCase()
const filteredItems = computed(() => {
  const search = query.value.trim().toLowerCase()
  return sourceItems.value
    .filter(item => !search || searchHaystack(item).includes(search))
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

const text = (values: Localized) => values[locale.value] || values.en || Object.values(values)[0] || ''
const channelName = (id: string) => channelMeta[locale.value][id]?.title || id
const resetPage = () => { page.value = 1 }
const setCategory = (value: string) => { category.value = value; resetPage() }
const initials = (name: string) => name.split(/\s+/).map(part => part[0]).join('').slice(0, 2).toUpperCase()
</script>

<template>
  <main class="resource-shell">
    <section class="resource-heading">
      <div>
        <h1>{{ meta.title }}</h1>
        <p>{{ meta.description }}</p>
      </div>
      <a class="submit-link" href="https://github.com/aidyou/chatspeed-res" target="_blank" rel="noopener">{{ t.submit }} <span>↗</span></a>
    </section>

    <div class="resource-layout">
      <aside class="resource-sidebar" :aria-label="t.ariaChannels">
        <div class="sidebar-section">
          <p class="sidebar-title">{{ t.channels }}</p>
          <a v-for="link in links" :key="link.id" class="channel-link" :class="{ active: link.id === props.channel }" :href="`${prefix}/${link.id}/`">
            <span class="channel-icon">{{ link.icon }}</span><span>{{ link.label }}</span><strong>{{ allItems.filter(item => item.channel === link.id).length }}</strong>
          </a>
          <a class="channel-link" :class="{ active: !props.channel }" :href="`${prefix}/`"><span class="channel-icon">✦</span><span>{{ t.allResources }}</span><strong>{{ allItems.length }}</strong></a>
        </div>
        <div v-if="props.channel" class="sidebar-section category-section">
          <p class="sidebar-title">{{ t.categories }}</p>
          <button class="category-link" :class="{ active: !category }" @click="setCategory('')"><span>{{ t.all }} {{ meta.title }}</span><strong>{{ sourceItems.length }}</strong></button>
          <button v-for="[name, count] in categories" :key="name" class="category-link" :class="{ active: category === name }" @click="setCategory(name)"><span>{{ name }}</span><strong>{{ count }}</strong></button>
        </div>
        <div class="sidebar-section sidebar-help">
          <p class="sidebar-title">{{ t.related }}</p>
          <a :href="`${prefix}/guide/`">{{ t.guide }} <span>→</span></a>
          <a href="https://aidyou.ai" target="_blank" rel="noopener">{{ t.site }} <span>↗</span></a>
        </div>
      </aside>

      <section class="resource-content" :aria-label="t.ariaList">
        <div class="content-toolbar">
          <div><h2>{{ t.contentTitle(meta.title) }}</h2><span>{{ t.count(filteredItems.length) }}</span></div>
          <label class="search-box"><span aria-hidden="true">⌕</span><input v-model="query" @input="resetPage" type="search" :placeholder="t.search(meta.title)" :aria-label="t.searchAria(meta.title)" /></label>
        </div>
        <div class="filter-row">
          <span class="filter-label">{{ t.filter }}</span>
          <button class="filter-chip" :class="{ selected: !category }" @click="setCategory('')">{{ t.allTags }}</button>
          <button v-for="[name] in categories.slice(0, 5)" :key="name" class="filter-chip" :class="{ selected: category === name }" @click="setCategory(name)">{{ name }}</button>
          <label class="sort-select">{{ t.sort }}<select v-model="sort" @change="resetPage"><option value="updated">{{ t.sortUpdated }}</option><option value="name">{{ t.sortName }}</option></select></label>
        </div>

        <div v-if="visibleItems.length" class="resource-list">
          <a v-for="item in visibleItems" :key="item.id" class="resource-card" :href="`${prefix}/${item.channel}/${item.id}.html`">
            <div class="card-top"><span class="resource-avatar">{{ initials(text(item.name)) }}</span><div class="card-title"><h3>{{ text(item.name) }}</h3><span class="status" :class="`status-${item.status}`">{{ statuses[item.status] }}</span></div><span class="card-arrow">→</span></div>
            <p class="card-description">{{ text(item.description) }}</p>
            <div class="card-tags"><span v-for="tag in item.tags.slice(0, 4)" :key="tag">{{ tag }}</span></div>
            <div class="card-meta"><span>{{ channelName(item.channel) }}</span><span>{{ t.verified }}{{ item.lastVerifiedAt }}</span></div>
          </a>
        </div>
        <div v-else class="empty-state"><strong>{{ t.emptyTitle }}</strong><span>{{ t.emptyHint }}</span><button @click="query = ''; setCategory('')">{{ t.emptyClear }}</button></div>

        <nav v-if="pageCount > 1" class="pagination" :aria-label="t.ariaPager">
          <button v-if="page > 1" @click="goPage(1)">{{ t.first }}</button>
          <button v-if="page > 1" @click="goPage(page - 1)">{{ t.prev }}</button>
          <button v-for="number in pageWindow" :key="number" :class="{ current: page === number }" :aria-current="page === number ? 'page' : undefined" @click="goPage(number)">{{ number }}</button>
          <button v-if="page < pageCount" @click="goPage(page + 1)">{{ t.next }}</button>
          <button v-if="page < pageCount" @click="goPage(pageCount)">{{ t.last }}</button>
        </nav>
      </section>
    </div>
  </main>
</template>
