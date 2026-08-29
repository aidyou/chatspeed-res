<script setup lang="ts">
import { computed, ref } from 'vue'

type Resource = {
  id: string
  name: Record<string, string>
  description: Record<string, string>
  categories: string[]
  tags: string[]
  detailPath: string
  searchText: string
}

const props = defineProps<{
  items: Resource[]
  locale?: 'en' | 'zh-Hans' | 'zh-Hant'
}>()

const query = ref('')
const category = ref('')
const locale = computed(() => props.locale || 'en')
const categories = computed(() => [...new Set(props.items.flatMap(item => item.categories))].sort())
const filteredItems = computed(() => {
  const search = query.value.trim().toLowerCase()
  return props.items.filter(item => {
    const matchesQuery = !search || item.searchText.includes(search)
    const matchesCategory = !category.value || item.categories.includes(category.value)
    return matchesQuery && matchesCategory
  })
})

const text = (values: Record<string, string>) => values[locale.value] || values.en || Object.values(values)[0] || ''
</script>

<template>
  <section class="resource-browser" aria-label="Resource browser">
    <div class="resource-filters">
      <input v-model="query" type="search" placeholder="Search resources" aria-label="Search resources" />
      <select v-model="category" aria-label="Filter by category">
        <option value="">All categories</option>
        <option v-for="item in categories" :key="item" :value="item">{{ item }}</option>
      </select>
    </div>
    <p class="resource-count">{{ filteredItems.length }} resources</p>
    <div class="resource-grid">
      <a v-for="item in filteredItems" :key="item.id" class="resource-card" :href="item.detailPath">
        <h2>{{ text(item.name) }}</h2>
        <p>{{ text(item.description) }}</p>
        <span>{{ item.categories.join(' · ') }}</span>
      </a>
    </div>
    <p v-if="filteredItems.length === 0" class="resource-empty">No resources found.</p>
  </section>
</template>

<style scoped>
.resource-filters { display: flex; gap: 0.75rem; margin: 1.5rem 0; }
.resource-filters input, .resource-filters select { border: 1px solid #d0d7de; border-radius: 0.5rem; padding: 0.65rem 0.8rem; font: inherit; }
.resource-filters input { flex: 1; }
.resource-count { color: #667085; }
.resource-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
.resource-card { display: block; border: 1px solid #e4e7ec; border-radius: 0.75rem; padding: 1rem; color: inherit; text-decoration: none; }
.resource-card:hover { border-color: #1677ff; }
.resource-card h2 { margin-top: 0; }
.resource-card p { color: #667085; min-height: 3rem; }
.resource-card span { font-size: 0.85rem; color: #1677ff; }
.resource-empty { padding: 2rem 0; color: #667085; }
@media (max-width: 600px) { .resource-filters { flex-direction: column; } }
</style>
