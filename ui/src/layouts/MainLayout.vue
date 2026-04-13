<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-avatar>
          <img src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20family%20seal%20red%20stamp%20design&image_size=square" alt="宗亲寻根">
        </q-avatar>
        <q-toolbar-title class="q-ml-md">
          <span class="text-h5" style="font-family: 'STXingkai', 'KaiTi', cursive;">宗亲寻根·薪火相传</span>
        </q-toolbar-title>
        <q-space />
        <q-btn flat label="首页" to="/" />
        <q-btn flat label="寻根" to="/xungen" />
        <q-btn flat label="族谱" to="/zupu" />
        <q-btn flat label="宗亲" to="/zongqin" />
        <q-btn flat label="我的" to="/profile" />
      </q-toolbar>
      <div class="header-decoration"></div>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-primary text-white">
      <q-toolbar class="justify-center">
        <div class="text-center">
          <div class="text-caption">宗亲寻根·薪火相传 © 2024</div>
          <div class="text-caption">弘扬中华优秀传统文化</div>
        </div>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script setup>
</script>

<style scoped>
</style>
