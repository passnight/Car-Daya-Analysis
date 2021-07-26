<template>
  <div id="Manager" style="display: flex; flex-direction: column">
    <el-row style="flex: none; display: flex; height: 60px">
      <div
        style="
          display: flex;
          align-items: center;
          margin-left: 10px;
          flex: none;
        "
      >
        <el-button stytle="color = #719cdc" @click="isCollapse = !isCollapse">
          <i class="el-icon-s-fold"></i>
        </el-button>
      </div>
      <el-menu
        class="el-menu-demo"
        mode="horizontal"
        router
        default-active="/feedback"
        @select="handleSelect"
        background-color="transparent"
        text-color="#fff"
        active-text-color="#ffd04b"
        style="flex: auto; display: flex"
      >
        <el-menu-item
          index="/sale"
          style="margin-left: 70px; margin-right: 10px"
          >销售分析</el-menu-item
        >
        <el-menu-item index="/feedback">用户反馈</el-menu-item>
        <el-menu-item index="/engineering" style="margin-left: auto"
          >指标分析</el-menu-item
        >
        <el-menu-item index="/manager" style="margin-right: 40px">用户管理</el-menu-item>
      </el-menu>
      <div
        style="
          margin-left: auto;
          display: flex;
          align-items: center;
          margin-right: 10px;
          flex: none;
        "
      >
        <el-dropdown>
          <i
            class="el-icon-setting"
            style="margin-right: 10px; color: #ffffff"
          ></i>
          <el-dropdown-menu slot="dropdown">
            <el-button @click="changeData">修改密码</el-button>
            <el-button @click="destoryUser">注销用户</el-button>
          </el-dropdown-menu>
        </el-dropdown>

        <span style="color: white"> 王小虎 </span>
      </div>
    </el-row>
    
    <el-container style="height: 500px; border: 1px solid #eee">
      <!-- <el-aside width="200px" style="background-color: #024195"> -->

     <el-menu
        style="flex: none"
        :default-openeds="['1', '2']"
        :collapse="isCollapse"
        :collapse-transition="false"
        background-color="rgba(35,81,162,0.5)"
        text-color="#fff"
        active-text-color="white"
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
     <el-table
    :data="tableData"
    size="medium"
    :cell-style="cellStyle"
    :header-cell-style="{
      color: '#fff',
      background: 'rgba(78, 131, 211, 0.8)',
    }"
    stripe
    :height="clientHeight - 62 < 370 ? 370 : clientHeight - 62"
  >
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
#Manager {
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
#Manager {
background: url("./Sale/test/home-background.png") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  background-position: top;

  margin: 0;
  padding: 0;
}
</style>
