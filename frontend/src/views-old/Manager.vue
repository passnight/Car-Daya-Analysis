<template>
  <div id="app">
    <el-row>
    
      <el-col style="height: 60px">

        <el-header style="text-align: right; font-size: 12px">
          
          <el-dropdown>
            <i
              class="el-icon-setting"
              style="margin-right: 15px; color: #ffffff"
            ></i>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item>修改密码</el-dropdown-item>
              <el-button @click="logoff">注销用户</el-button>
            </el-dropdown-menu>
          </el-dropdown>
          <span>王小虎</span>
        </el-header>
      </el-col>
    </el-row>
    <el-row>
      <el-button style="color = transprant" @click="isCollapse = !isCollapse"
        ><i class="el-icon-s-fold"></i
      >
      </el-button>
    </el-row>
    <el-container style="height: 500px; border: 1px solid #eee">
      <!-- <el-aside width="200px" style="background-color: #024195"> -->

      <el-menu
        :default-openeds="['1', '2']"
        :collapse="isCollapse"
        :collapse-transition="false"
      >
        <el-submenu index="1">
          <template slot="title">
            <i class="el-icon-message"></i>
            <span slot="title">填写用户信息</span>
          </template>
          <el-menu-item-group>
            <template slot="title">填写用户名</template>
            <el-input placeholder="请输入用户名" v-model="input" clearable>
            </el-input>
          </el-menu-item-group>

          <el-menu-item-group>
            <template slot="title">填写用户密码</template>
            <el-input placeholder="请输入用户密码" v-model="input" clearable>
            </el-input>
          </el-menu-item-group>

          <el-menu-item-group>
            <template slot="title">填写新的用户密码</template>
            <el-input placeholder="请输入新的用户密码" v-model="input" clearable>
            </el-input>
          </el-menu-item-group>

          
        </el-submenu>
        <el-submenu index="2">
          <template slot="title">
            <i class="el-icon-menu"></i>
            <span slot="title">功能选择</span>
          </template>
          <el-menu-item-group> 
                   <el-menu-item>
               <el-button type="text" @click="myadd"> 添加用户信息 </el-button>
                   </el-menu-item>
                  <el-menu-item>
               <el-button type="text" @click="mychange">修改用户信息</el-button>
                 </el-menu-item>
                   <el-menu-item>
               <el-button type="text" @click="mydel">删除目标用户</el-button>
                 </el-menu-item>
         
          </el-menu-item-group>
        </el-submenu>
       
      </el-menu>
      <!-- </el-aside> -->
      <el-container>
    <el-main>
      <el-table :data="tableData">
        <el-table-column prop="date" label="日期" width="140">
        </el-table-column>
        <el-table-column prop="name" label="姓名" width="120">
        </el-table-column>
        <el-table-column prop="password" label="密码">
        </el-table-column>
      </el-table>
    </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script>
export default {
 
    data() {
      const item = {
        date: '2111-11-11',
        name: '路人甲',
        password: '000000'
      };
      return {
         isCollapse: false,
        tableData: Array(10).fill(item)
      }
    },

  methods: {
    //注销用户
    logoff() {
      this.$confirm("此操作将永久删除该用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "删除成功!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
     //添加用户
    myadd() {
      this.$confirm("您正在添加一名新的用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "删除成功!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
     //修改用户
    mychange() {
      this.$confirm("您正在修改用户的信息, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "删除成功!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },
     //删除用户
    mydel() {
      this.$confirm("您正在删除用户, 是否继续?", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          this.$message({
            type: "success",
            message: "删除成功!",
          });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "已取消删除",
          });
        });
    },

  },
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.el-header {
  background-color: #134194;
  color: #ffffff;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
#app {
  margin: 0;
  padding: 0;
}
</style>
