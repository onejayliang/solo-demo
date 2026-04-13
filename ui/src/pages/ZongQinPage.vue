<template>
  <q-page class="row items-start justify-center q-pa-xl">
    <div class="col-12 col-md-10 col-xl-8">
      <q-card class="traditional-border q-mb-xl">
        <q-card-section>
          <h2 class="text-h4 text-primary" style="font-family: 'STKaiti', 'KaiTi', serif;">
            <q-icon name="people" class="q-mr-sm" />宗亲互动
          </h2>
        </q-card-section>
        <q-card-section>
          <p class="text-body1 text-secondary">专属聊天室、宗族活动、祖训家风分享，宗亲交流平台</p>
        </q-card-section>
      </q-card>

      <q-tabs v-model="activeTab" class="bg-white q-mb-xl">
        <q-tab name="chat" label="聊天室" icon="chat" />
        <q-tab name="activities" label="活动" icon="event" />
        <q-tab name="culture" label="家风" icon="book" />
      </q-tabs>

      <q-tab-panels v-model="activeTab" animated>
        <q-tab-panel name="chat">
          <q-card class="traditional-border q-mb-md" v-for="room in chatRooms" :key="room.id">
            <q-card-section class="row items-center cursor-pointer">
              <div class="col-2">
                <q-avatar size="56px" :color="room.color">{{ room.name.charAt(0) }}</q-avatar>
              </div>
              <div class="col-7">
                <h4 class="text-h6 text-primary">{{ room.name }}</h4>
                <p class="text-caption text-secondary">{{ room.lastMessage }}</p>
              </div>
              <div class="col-3 text-right">
                <q-chip v-if="room.unread" size="xs" color="red">{{ room.unread }}</q-chip>
              </div>
            </q-card-section>
          </q-card>
        </q-tab-panel>

        <q-tab-panel name="activities">
          <q-card class="traditional-border q-mb-md" v-for="activity in activities" :key="activity.id">
            <q-img :src="activity.image" ratio="16:9" />
            <q-card-section>
              <h4 class="text-h6 text-primary">{{ activity.title }}</h4>
              <p class="text-caption text-secondary">
                <q-icon name="event" size="14px" class="q-mr-xs" />
                {{ activity.date }}
              </p>
              <p class="text-caption text-secondary">
                <q-icon name="place" size="14px" class="q-mr-xs" />
                {{ activity.location }}
              </p>
              <p class="text-body2 q-mt-sm">{{ activity.description }}</p>
            </q-card-section>
            <q-card-actions align="right">
              <q-btn color="primary" label="报名参加" />
            </q-card-actions>
          </q-card>
        </q-tab-panel>

        <q-tab-panel name="culture">
          <q-card class="traditional-border q-mb-md" v-for="item in cultureItems" :key="item.id">
            <q-card-section>
              <div class="row items-start">
                <q-avatar class="q-mr-md">
                  <img :src="item.avatar" alt="avatar">
                </q-avatar>
                <div class="col">
                  <h4 class="text-h6 text-primary">{{ item.author }}</h4>
                  <p class="text-caption text-secondary q-mb-sm">{{ item.time }}</p>
                  <p class="text-body1">{{ item.content }}</p>
                </div>
              </div>
            </q-card-section>
            <q-separator />
            <q-card-actions>
              <q-btn flat icon="thumb_up" label="点赞" />
              <q-btn flat icon="chat_bubble" label="评论" />
              <q-btn flat icon="share" label="分享" />
            </q-card-actions>
          </q-card>
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue';

const activeTab = ref('chat');

const chatRooms = ref([
  { id: 1, name: '陇西李氏宗亲群', lastMessage: '李氏族谱更新了', unread: 5, color: 'primary' },
  { id: 2, name: '太原王氏宗亲群', lastMessage: '下周祭祖活动', unread: 0, color: 'secondary' }
]);

const activities = ref([
  {
    id: 1,
    title: '李氏宗亲祭祖大典',
    date: '2024-04-20 09:00',
    location: '陇西李氏宗祠',
    description: '一年一度的李氏宗亲祭祖大典，欢迎各地宗亲参加',
    image: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20ancestor%20worship%20ceremony&image_size=landscape_16_9'
  }
]);

const cultureItems = ref([
  {
    id: 1,
    author: '李明',
    time: '2天前',
    avatar: 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=traditional%20chinese%20avatar%20portrait&image_size=square',
    content: '李氏祖训：忠孝传家，耕读为本。希望后世子孙牢记祖训，传承家风。'
  }
]);
</script>

<style scoped>
</style>
