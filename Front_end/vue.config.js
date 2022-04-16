const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// module.exports = { 
//   devServer: { 
//     proxy: { 
//       '/api': { 
//         target: 'http://localhost:8090/',
//         changeOrigin: true, 
//         pathRewrite: { 
//           '^/api': ''
//         } 
//       } 
//     } 
//   },
//   outputDir: '../Back_end/build'
// }
