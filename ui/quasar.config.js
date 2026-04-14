const { configure } = require('quasar/wrappers');

module.exports = configure(function (/* ctx */) {
  return {
    eslint: {
      warnings: false,
      errors: false
    },

    boot: [],

    css: [
      'app.scss'
    ],

    extras: [
      'roboto-font',
      'material-icons',
      'mdi-v7'
    ],

    build: {
      target: {
        browser: ['es2019', 'edge88', 'firefox78', 'chrome87', 'safari13.1'],
        node: 'node16'
      },
      vueRouterMode: 'history',
      vitePlugins: []
    },

    devServer: {
      open: true,
      port: 8080,
      proxy: {
        '/api': {
          target: 'http://localhost:7000',
          changeOrigin: true,
          pathRewrite: {
            '^/api': '/api'
          }
        }
      }
    },

    framework: {
      config: {},
      plugins: [
        'Notify',
        'Dialog',
        'Loading'
      ],
      components: [
        'QLayout',
        'QHeader',
        'QFooter',
        'QPageContainer',
        'QPage',
        'QToolbar',
        'QToolbarTitle',
        'QBtn',
        'QSpace',
        'QAvatar',
        'QCard',
        'QCardSection',
        'QIcon',
        'QImg',
        'QRow',
        'QCol'
      ]
    },

    animations: [],

    ssr: {
      pwa: false,
      prodPort: 3000,
      maxAge: 1000 * 60 * 60 * 24 * 30,
      middlewares: [
        'render'
      ]
    },

    pwa: {
      workboxPluginMode: 'GenerateSW',
      workboxOptions: {},
      manifest: {
        name: '宗亲寻根·薪火相传',
        short_name: '宗亲寻根',
        description: '宗亲寻根·薪火相传APP',
        display: 'standalone',
        orientation: 'portrait',
        background_color: '#ffffff',
        theme_color: '#8B4513',
        icons: [
          {
            src: 'icons/icon-128x128.png',
            sizes: '128x128',
            type: 'image/png'
          }
        ]
      }
    },

    cordova: {},

    capacitor: {
      hideSplashscreen: true
    },

    electron: {
      inspectPort: 5858,
      bundler: 'packager',
      packager: {},
      builder: {
        appId: 'zongqin-xungen'
      }
    },

    bex: {
      contentScripts: [
        'my-content-script'
      ]
    }
  }
});
