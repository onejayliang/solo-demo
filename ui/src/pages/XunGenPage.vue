<template>
  <q-page class="row items-start justify-center q-pa-xl">
    <div class="col-12 col-md-10 col-xl-8">
      <q-card class="traditional-border q-mb-xl">
        <q-card-section>
          <h2 class="text-h4 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">
            <q-icon name="compass" class="q-mr-sm" />寻根问祖
          </h2>
        </q-card-section>
        <q-card-section>
          <p class="text-body1 text-secondary">提交祖上资料，通过大数据智能匹配，寻找您的宗族归属</p>
        </q-card-section>
      </q-card>

      <q-card class="traditional-border q-mb-xl">
        <q-card-section>
          <h3 class="text-h5 text-primary">提交祖上资料</h3>
        </q-card-section>
        <q-card-section class="q-pa-lg">
          <q-form class="q-gutter-md">
            <div class="row">
              <div class="col-12 col-md-6">
                <q-input filled v-model="form.surname" label="姓氏" />
              </div>
              <div class="col-12 col-md-6">
                <q-input filled v-model="form.hallName" label="堂号" />
              </div>
            </div>
            <q-input filled v-model="form.ancestor" label="始祖信息" />
            <q-input filled v-model="form.origin" label="发源地" />
            <q-textarea filled v-model="form.description" label="详细描述" rows="4" />
            <q-card-actions align="right">
              <q-btn color="primary" label="提交资料" @click="submitData" />
            </q-card-actions>
          </q-form>
        </q-card-section>
      </q-card>

      <q-card class="traditional-border">
        <q-card-section>
          <h3 class="text-h5 text-primary">匹配结果</h3>
        </q-card-section>
        <q-card-section class="q-pa-lg">
          <div class="row q-gutter-md">
            <div class="col-12" v-for="match in matches" :key="match.id">
              <q-card flat bordered>
                <q-card-section>
                  <div class="row items-center">
                    <div class="col-12 col-md-8">
                      <h4 class="text-h6 text-primary">{{ match.clanName }}</h4>
                      <p class="text-caption text-secondary">匹配度: {{ match.matchRate }}%</p>
                      <p class="text-body2 q-mt-sm">{{ match.description }}</p>
                    </div>
                    <div class="col-12 col-md-4 text-right">
                      <q-btn color="primary" label="申请认祖" size="md" />
                    </div>
                  </div>
                </q-card-section>
              </q-card>
            </div>
            <div class="col-12 text-center text-secondary" v-if="matches.length === 0">
              <p>暂无匹配结果，请先提交祖上资料</p>
            </div>
          </div>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';
import { useQuasar } from 'quasar';

const $q = useQuasar();

const form = ref({
  surname: '',
  hallName: '',
  ancestor: '',
  origin: '',
  description: ''
});

const matches = ref([
  {
    id: 1,
    clanName: '陇西李氏',
    matchRate: 92,
    description: '始祖李利贞，发源地陇西，堂号陇西堂'
  },
  {
    id: 2,
    clanName: '太原王氏',
    matchRate: 78,
    description: '始祖太子晋，发源地太原，堂号太原堂'
  }
]);

const submitData = () => {
  $q.notify({
    type: 'positive',
    message: '资料提交成功，正在进行智能匹配...'
  });
};
</script>

<style scoped>
</style>
