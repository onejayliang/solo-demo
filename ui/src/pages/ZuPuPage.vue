<template>
  <q-page class="row items-start justify-center q-pa-xl">
    <div class="col-12 col-md-10 col-xl-8">
      <q-card class="traditional-border q-mb-xl">
        <q-card-section class="row items-center justify-between">
          <h2 class="text-h4 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">
            <q-icon name="menu_book" class="q-mr-sm" />族谱管理
          </h2>
          <q-btn color="primary" label="创建族谱" icon="add" />
        </q-card-section>
        <q-card-section>
          <p class="text-body1 text-secondary">数字化族谱，传承家族历史，支持创建、编辑和查阅族谱</p>
        </q-card-section>
      </q-card>

      <div class="row q-gutter-md">
        <div class="col-12 col-md-6" v-for="genealogy in genealogies" :key="genealogy.id">
          <q-card class="traditional-border">
            <q-img
              :src="genealogy.image"
              ratio="16:9"
            />
            <q-card-section>
              <h3 class="text-h5 text-primary">{{ genealogy.name }}</h3>
              <p class="text-caption text-secondary">
                <q-icon name="people" size="14px" class="q-mr-xs" />
                {{ genealogy.memberCount }}位族人
              </p>
              <p class="text-body2 q-mt-sm">{{ genealogy.description }}</p>
            </q-card-section>
            <q-card-actions align="right">
              <q-btn flat label="查看" color="primary" />
              <q-btn flat label="编辑" color="secondary" />
            </q-card-actions>
          </q-card>
        </div>
      </div>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';

const genealogies = ref([
  {
    id: 1,
    name: '陇西李氏宗谱',
    memberCount: 1256,
    description: '记录陇西李氏一脉的繁衍历史，始于唐代，至今已有千年历史',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20genealogy%20book%20family%20tree&image_size=landscape_16_9'
  },
  {
    id: 2,
    name: '太原王氏族谱',
    memberCount: 892,
    description: '太原王氏宗族谱牒，详细记载了王氏族人的世系传承',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=ancient%20chinese%20family%20tree%20scroll%20traditional&image_size=landscape_16_9'
  }
]);
</script>

<style scoped>
</style>
