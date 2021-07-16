<template>
  <el-container>
    <el-main>
      <div class="demo-image__placeholder">
        <div class="block">
          <span class="demonstration">自定义</span>
          <el-image :src="src" :fit="scale - down">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
</template>


<script>
export default {
  name: "Fuel",
  data() {
    return {
      src: "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
    };
  },
};
</script>