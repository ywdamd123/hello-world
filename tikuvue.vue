<template>
  
    <a-button type="primary" class="start" v-if="Start" v-on:click="start">开始</a-button>
  
  <div class="change" v-show="change">
      <div class="big">
          <div class="num">
              {{ count }}
          </div>
  
          <div class="question">
            {{ obj0.question[count] }}
          </div>
  
<!--           
            <template v-for="(i , index) in question">
              <a-radio-group  v-model.lazy="value"  v-show="index == count" v-bind:name="index">
            <a-radio :style="radioStyle" v-bind:value="obj0.a[index]">{{ obj0.a[count] }}</a-radio>
            <a-radio :style="radioStyle" v-bind:value="obj0.b[index]">{{ obj0.b[count] }}</a-radio>
            <a-radio :style="radioStyle" v-bind:value="obj0.c[index]">{{ obj0.c[count] }}</a-radio>
            <a-radio :style="radioStyle" v-bind:value="obj0.d[index]">{{ obj0.d[count] }}</a-radio>
            </a-radio-group> 
            </template> -->
            
            <template v-for="(i , index) in obj0.a">
              <div   v-show="index == count">
            <input type="radio" v-bind:name="index" v-bind:value="obj0.a[index]" >{{ obj0.a[count]  }} 
            <input type="radio" v-bind:name="index"v-bind:value="obj0.b[index]">{{ obj0.b[count] }}
            <input type="radio"  v-bind:name="index"v-bind:value="obj0.c[index]">{{ obj0.c[count] }}
            <input type="radio"  v-bind:name="index"v-bind:value="obj0.d[index]">{{ obj0.d[count] }}
            </div> 
            </template>
        
      </div>
      
     <a-button class="prev" v-on:click="prev">上一题</a-button>
     <a-button class="next" @click="next">下一题</a-button>

     <a-button class="submit" v-on:click="submit1">提交</a-button> <br>
     <a-button class="show_database" @click="show_database">查看数据库</a-button> <br>
     <a-button class="disappear_database" @click="disappear_database">关闭数据库</a-button>
      
     <table v-if="database">
      <tbody>
        <tr>
          <th>ID</th>
          <th>题目</th>
          <th>选项</th>
          <th>答案</th>
       </tr>
          <tr v-for="(i , index) in obj0.a">
             <td>{{ index }}</td>
             <td>{{ obj0.question[index] }}</td>
             <td>A:{{ obj0.a[index] }} B:{{ obj0.b[index]}} C:{{ obj0.c[index] }} D:{{ obj0.d[index] }}</td>
             <td>{{ obj0.ans[index]}}</td>
          </tr>
      </tbody>
     </table> <br>
  
     <a-button class="append" v-show="cancle" @click="appended">添加</a-button>
     
          <form action="" class="appended" v-if="append" id="new" >
             <br>
            <a-space direction="vertical">
              题目<a-input v-model:value="value1"  />
      选项<a-input v-model:value="value2" placeholder="A" />
      <a-input v-model:value="value3"  placeholder="B"/>
      <a-input v-model:value="value4" placeholder="C" />
      <a-input v-model:value="value5"  placeholder="D"/>
      答案<a-input v-model:value="value6"  />
  
      <a-button class="sure" v-on:click="submit">确认</a-button>
            <a-button class="cancle" v-show="cancleed" v-on:click="quxiao">取消</a-button>
        </a-space>
            </form>
          
  </div>
  </template>
  
  <script setup>
  import { ref, reactive} from 'vue';

  // 按钮显示隐藏
  const change = ref(false)
  const Start = ref(true)
  const cancle = ref(false)
  const append = ref(false)
  const cancleed = ref(false)
    const start = () => {
      Start.value =! Start.value
      change.value =! change.value
    }
  
  const database = ref(false)
  const show_database =  ()  => {
    database.value = true
    cancle.value = true
  }
  const disappear_database = () => {
    database.value = false
    cancle.value = false
  }
  
  const appended = () => {
    append.value = true
    cancleed.value = true
  }
  
  const quxiao = () => {
    append.value = false
    cancleed.value = false
  }
  
  // 输入框
  const value1 = ref('')
  const value2 = ref('')
  const value3 = ref('')
  const value4 = ref('')
  const value5 = ref('')
  const value6 = ref('')
  
  const obj0 = reactive({
                  question: ['起风了'],
                  a: ['1111'],
                  b: ['2222'],
                  c: ['3333'],
                  d: ['4444'],
                  ans: ['2222']
          })
// 当前题目序号
  const count = ref(0)
  
  // 上一题
  const prev =  () => {
    if (count.value > 0) {
      count.value--
    }
  }
  
  // 下一题
  const next =  () => {
    if (count.value < obj0.a.length - 1) {
      count.value++
    }
  }
  
  // const value = ref(1);
  // const radioStyle = reactive({
  //   display: 'flex',
  //   height: '30px',
  //   lineHeight: '30px',
  // });
  
  // 添加题目
  const submit = () => {
    
    if ( value1.value === '' || value2.value === '' || value3.value === '' || value4.value === '' || value5.value === '' || value6.value === '') {
  
      alert('输入不完全')
    }else {
     
     obj0.question.push(value1.value)
     obj0.a.push(value2.value)
     obj0.b.push(value3.value)
     obj0.c.push(value4.value)
     obj0.d.push(value5.value)
     obj0.ans.push(value6.value)
  
     append.value = false
    // 清空输入框
    value1.value = ''
    value2.value = ''
    value3.value = ''
    value4.value = ''
    value5.value = ''
    value6.value = ''

    }
  }
  
  const submit1 = () => {
    while (true) {
                  // 捕获已勾选的答案
                  const opt = document.querySelectorAll('input:checked')
                  
                  // 表示答对的题数
                  let correct = 0
                  // 提示未答完，同时保证下面遍历答案的for循环不出错
                  if (opt.length < obj0.a.length) {
                      alert('有题目未作答')
                      break
                  }
                  
                  // obj0.a.length是题目数
                  for (let i = 0; i <= obj0.a.length - 1; i++) {
                    
                      // 判断对错并记录
                          if (opt[i].value === obj0.ans[i]) {
                              correct++
                          }
                  }
                  alert(`答对了${correct}道题`)
                  break
              }
  }
  </script>
  
  <style scoped>
        table,th, td{
          width: 350px;
          border:  1px solid black;
          border-collapse: collapse;
        }
  </style>