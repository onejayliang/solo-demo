import api from './api';

export const ChatService = {
  /**
   * 发送消息
   * @param {String} chatRoomId - 聊天室ID
   * @param {Object} message - 消息内容
   * @returns {Promise<Object>} 发送结果
   */
  sendMessage(chatRoomId, message) {
    return api.post(`/chat/${chatRoomId}/messages`, message);
  },

  /**
   * 获取聊天室列表
   * @returns {Promise<Object>} 聊天室列表
   */
  getChatRooms() {
    return api.get('/chat/rooms');
  },

  /**
   * 获取聊天室消息
   * @param {String} chatRoomId - 聊天室ID
   * @param {Number} limit - 消息数量
   * @param {String} before - 分页标记
   * @returns {Promise<Object>} 消息列表
   */
  getMessages(chatRoomId, limit = 20, before = null) {
    let url = `/chat/${chatRoomId}/messages?limit=${limit}`;
    if (before) {
      url += `&before=${before}`;
    }
    return api.get(url);
  },

  /**
   * 创建活动
   * @param {Object} activity - 活动信息
   * @returns {Promise<Object>} 创建结果
   */
  createActivity(activity) {
    return api.post('/activity/create', activity);
  },

  /**
   * 获取活动列表
   * @returns {Promise<Object>} 活动列表
   */
  getActivities() {
    return api.get('/activity/list');
  },

  /**
   * 报名活动
   * @param {String} activityId - 活动ID
   * @returns {Promise<Object>} 报名结果
   */
  joinActivity(activityId) {
    return api.post(`/activity/${activityId}/join`);
  },

  /**
   * 分享家风
   * @param {Object} culture - 家风信息
   * @returns {Promise<Object>} 分享结果
   */
  shareCulture(culture) {
    return api.post('/culture/share', culture);
  },

  /**
   * 获取家风列表
   * @returns {Promise<Object>} 家风列表
   */
  getCultures() {
    return api.get('/culture/list');
  },

  /**
   * 获取宗亲名片
   * @returns {Promise<Object>} 名片信息
   */
  getZongQinCard() {
    return api.get('/user/zongqin-card');
  }
};
