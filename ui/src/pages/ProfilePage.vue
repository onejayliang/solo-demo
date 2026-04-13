<template>
  <q-page class="row items-start justify-center q-pa-xl">
    <div class="col-12 col-md-10 col-xl-8">
      <q-card class="traditional-border q-mb-xl">
        <q-card-section class="bg-amber-50 text-center">
          <q-avatar size="120px" class="q-mb-md">
            <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20portrait%20avatar&image_size=square" alt="avatar">
          </q-avatar>
          <h2 class="text-h4 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">
            {{ profile.name }}
          </h2>
          <p class="text-subtitle1 text-secondary">{{ profile.clan }}</p>
          <div class="seal-stamp q-mt-md">{{ profile.styleName }}</div>
        </q-card-section>
      </q-card>

      <q-card class="traditional-border q-mb-xl">
        <q-card-section>
          <h3 class="text-h5 text-primary">基本信息</h3>
        </q-card-section>
        <q-list bordered>
          <q-item>
            <q-item-section avatar>
              <q-icon name="person" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>姓名</q-item-label>
              <q-item-label caption>{{ profile.name }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section avatar>
              <q-icon name="family_restroom" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>宗族</q-item-label>
              <q-item-label caption>{{ profile.clan }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section avatar>
              <q-icon name="badge" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>辈分</q-item-label>
              <q-item-label caption>{{ profile.generation }}</q-item-label>
            </q-item-section>
          </q-item>
          <q-item>
            <q-item-section avatar>
              <q-icon name="edit" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>表字</q-item-label>
              <q-item-label caption>{{ profile.styleName }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card>

      <q-card class="traditional-border q-mb-xl">
        <q-card-section>
          <h3 class="text-h5 text-primary">功能菜单</h3>
        </q-card-section>
        <q-list bordered>
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="settings" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>账号设置</q-item-label>
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="notifications" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>消息通知</q-item-label>
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="help" color="primary" />
            </q-item-section>
            <q-item-section>
              <q-item-label>帮助中心</q-item-label>
            </q-item-section>
          </q-item>
          <q-item clickable v-ripple>
            <q-item-section avatar>
              <q-icon name="logout" color="negative" />
            </q-item-section>
            <q-item-section>
              <q-item-label class="text-negative">退出登录</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';

const profile = ref({
  name: '李明',
  clan: '陇西李氏',
  generation: '第28代',
  styleName: '明远'
});
</script>

<style scoped>
</style>
