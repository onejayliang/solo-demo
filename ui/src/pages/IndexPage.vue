<template>
  <q-page class="row items-start justify-center q-pa-xl">
    <div class="col-12 col-md-10 col-xl-8">
      <q-card class="traditional-border q-mb-xl">
        <q-card-section class="text-center bg-amber-50">
          <div class="seal-stamp q-mb-md">宗亲寻根</div>
          <h1 class="text-h3 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">
            宗亲寻根·薪火相传
          </h1>
          <p class="text-subtitle1 text-secondary q-mt-md">
            认祖归亲 · 族谱信息化 · 宗亲互动
          </p>
        </q-card-section>
        
        <q-card-section class="q-pa-xl">
          <div class="row q-gutter-xl">
            <div class="col-12 col-md-4">
              <q-card flat bordered class="cursor-pointer" @click="$router.push('/xungen')">
                <q-card-section class="text-center">
                  <q-icon name="compass" size="5rem" color="primary" />
                  <h3 class="text-h5 q-mt-md">寻根问祖</h3>
                  <p class="text-caption q-mt-sm">大数据智能匹配，助力认祖归亲</p>
                </q-card-section>
              </q-card>
            </div>
            
            <div class="col-12 col-md-4">
              <q-card flat bordered class="cursor-pointer" @click="$router.push('/zupu')">
                <q-card-section class="text-center">
                  <q-icon name="menu_book" size="5rem" color="primary" />
                  <h3 class="text-h5 q-mt-md">族谱管理</h3>
                  <p class="text-caption q-mt-sm">数字化族谱，传承家族历史</p>
                </q-card-section>
              </q-card>
            </div>
            
            <div class="col-12 col-md-4">
              <q-card flat bordered class="cursor-pointer" @click="$router.push('/zongqin')">
                <q-card-section class="text-center">
                  <q-icon name="people" size="5rem" color="primary" />
                  <h3 class="text-h5 q-mt-md">宗亲互动</h3>
                  <p class="text-caption q-mt-sm">专属聊天室，宗亲交流平台</p>
                </q-card-section>
              </q-card>
            </div>
          </div>
        </q-card-section>
      </q-card>

      <q-card class="traditional-border">
        <q-card-section>
          <h2 class="text-h4 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">
            宗族文化传承
          </h2>
        </q-card-section>
        <q-card-section class="q-pa-lg">
          <div class="row q-gutter-lg">
            <div class="col-12">
              <q-img
                src="https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20ancestor%20hall%20family%20tree%20culture&image_size=landscape_16_9"
                ratio="16:9"
                class="rounded-borders"
              />
            </div>
            <div class="col-12 q-mt-md">
              <p class="text-body1 text-secondary">
                宗族文化是中华传统文化的重要组成部分，承载着家族血脉延续、文化传承的重要使命。
                本平台致力于推动传统族谱信息化、数字化保存，帮助流失在外的族人认祖归亲，
                重建宗亲联系，弘扬中华优秀传统文化。
              </p>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
</script>

<style scoped>
</style>
