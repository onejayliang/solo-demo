<template>
  <q-page class="row items-center justify-center" style="min-height: 100vh; background: linear-gradient(135deg, #FFF8DC 0%, #FAEBD7 100%);">
    <q-card class="traditional-border" style="width: 100%; max-width: 450px;">
      <q-card-section class="text-center bg-amber-50">
        <div class="seal-stamp q-mb-md">宗亲寻根</div>
        <h2 class="text-h4 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">用户登录</h2>
      </q-card-section>
      
      <q-card-section class="q-pa-xl">
        <q-form @submit="handleLogin" class="q-gutter-md">
          <q-input
            filled
            v-model="form.username"
            label="用户名"
            type="text"
            :rules="[val => !!val || '请输入用户名']"
          />
          
          <q-input
            filled
            v-model="form.password"
            label="密码"
            type="password"
            :rules="[val => !!val || '请输入密码']"
          />
          
          <q-card-actions align="center" class="q-mt-lg">
            <q-btn type="submit" color="primary" label="登录" size="lg" class="q-mr-md" />
            <q-btn color="secondary" label="注册" size="lg" flat />
          </q-card-actions>
        </q-form>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useQuasar } from 'quasar';

const router = useRouter();
const $q = useQuasar();

const form = ref({
  username: '',
  password: ''
});

const handleLogin = () => {
  $q.loading.show({
    message: '登录中...'
  });
  
  setTimeout(() => {
    $q.loading.hide();
    $q.notify({
      type: 'positive',
      message: '登录成功'
    });
    router.push('/');
  }, 1000);
};
</script>

<style scoped>
</style>
