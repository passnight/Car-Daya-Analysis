<template>
<el-contianer>
     <el-container>
      <el-container>
    <el-main>
      <div class="demo-image__placeholder">
        <div id="block" style="display: flex; flex-direction: column">
     
          <el-image :src="src" :fit="scale - down">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
   <el-container>
    <el-main>
      <div class="demo-image__placeholder">
       <div id="block" style="display: flex; flex-direction: column">
        
          <el-image :src="src" :fit="scale - down">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
 </el-container>


  <el-container>
      <el-container>
    <el-main>
      <div class="demo-image__placeholder">
        <div id="block" style="display: flex; flex-direction: column">

          <el-image :src="src" :fit="scale - down">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
   <el-container>
    <el-main>
      <div class="demo-image__placeholder">
         <div id="block" style="display: flex; flex-direction: column">
          <el-image :src="src" :fit="scale - down">
            <div slot="placeholder" class="image-slot">
              加载中<span class="dot">...</span>
            </div>
          </el-image>
        </div>
      </div>
    </el-main>
  </el-container>
 </el-container>
</el-contianer>
 
</template>


<script>
export default {
  name: "chapter",
  data() {
    return {
      src: "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
    };
  },
};
</script>