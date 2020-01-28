<template>
  <div class="dreams">
    <h1>{{ msg }}</h1>
    <el-form ref="postForm" :model="postForm" label-width="150px" class="form-container" :rules="rules"
             label-position="left">
      <el-row>
        <el-col :span="12">
          <el-form-item label="First Name" class="postInfo-container-item" prop="firstname">
            <el-input style="width:200px" v-model="postForm.firstname"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="Last Name" class="postInfo-container-item" prop="lastname">
            <el-input style="width:200px" v-model="postForm.lastname"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="12">
          <el-form-item label="University" class="postInfo-container-item" prop="university">
            <el-input style="width:350px" v-model="postForm.university"></el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="Qualification" class="postInfo-container-item" prop="qualification">
            <el-select style="width:200px" v-model="postForm.qualification">
              <el-option label="Bachelor" value="Bachelor"></el-option>
              <el-option label="Master" value="Master"></el-option>
              <el-option label="Phd" value="Phd"></el-option>
              <el-option label="Others" value="Others"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <el-form-item label="Subject" class="postInfo-container-item" prop="subject">
            <el-input style="width:350px" v-model="postForm.subject"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <el-form-item label="Year of Study" class="postInfo-container-item" prop="year">
            <el-select v-model="postForm.year" placeholder="please select your year">
              <el-option label="Year 1" value="year1"></el-option>
              <el-option label="Year 2" value="year2"></el-option>
              <el-option label="Year 3" value="year3"></el-option>
              <el-option label="Year 4" value="year4"></el-option>
            </el-select>
          </el-form-item>
        </el-col>
      </el-row>
      <!--      <el-row>-->
      <!--        <el-col :span="8">-->
      <!--          <el-form-item label="Status" prop="status">-->
      <!--            <el-radio v-model="radio" label="1">Studing</el-radio>-->
      <!--            <el-radio v-model="radio" label="2">Working</el-radio>-->
      <!--          </el-form-item>-->
      <!--        </el-col>-->
      <!--      </el-row>-->
      <!--      <transition name="fade">-->
      <!--        <div v-show="radio=='2'">-->
      <!--          <el-row>-->
      <!--            <el-col :span="12">-->
      <!--              <el-form-item label="Current Company" class="postInfo-container-item">-->
      <!--                <el-input style="width:300px" v-model="postForm.currentjobcompany"></el-input>-->
      <!--              </el-form-item>-->
      <!--            </el-col>-->
      <!--            <el-col :span="12">-->
      <!--              <el-form-item label="Current Job Title" class="postInfo-container-item">-->
      <!--                <el-input style="width:300px" v-model="postForm.currentjobtitle"></el-input>-->
      <!--              </el-form-item>-->
      <!--            </el-col>-->
      <!--          </el-row>-->
      <!--        </div>-->
      <!--      </transition>-->
      <el-row>
        <el-col :span="24">
          <el-form-item label="Preferred Role" class="postInfo-container-item" prop="expected">
            <el-checkbox-group v-model="expectedcheck">
              <el-checkbox v-for="expect in expectedlist" :label="expect" :key="expect"></el-checkbox>
            </el-checkbox-group>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <el-form-item label="E-mail" class="postInfo-container-item" prop="email">
            <el-input style="width:400px" v-model="postForm.email"></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="24">
          <el-form-item prop="textarea" label="Comments">
            <el-input
              type="textarea"
              :autosize="{ minRows: 5, maxRows: 20}"
              placeholder="Please type your comments here"
              maxlength="1000"
              show-word-limit
              v-model="postForm.textarea">
            </el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-form-item style="text-align: center;margin-top: 20px">
        <el-button type="primary" @click="submitForm('postForm')">Submit</el-button>
        <el-button @click="resetForm('postForm')">Reset</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
    import axios from 'axios'
    import qs from 'qs';

    export default {
        name: 'HelloWorld',
        data() {
            return {
                msg: 'Welcome to DreamsAI',
                postForm: {
                    lastname: '',
                    firstname: '',
                    university: '',
                    qualification: '',
                    subject: '',
                    year: '',
                    expected: '',
                    email: '',
                    // currentjobcompany: '',
                    // currentjobtitle: '',
                    textarea: ''
                },
                expectedlist: ["{ML} Model Researcher", "{ML} Model/ Software Developer", "Firefighting Coder", "Front End Developer", "Data Scientist", "Knowledge Engineer", "System Architect", "DevOps Architect"],
                expectedcheck: [],
                radio: '1',
                rules: {
                    lastname: [
                        {required: true, message: 'please enter Last Name', trigger: 'blur'}
                    ],
                    firstname: [
                        {required: true, message: 'please enter First Name', trigger: 'blur'}
                    ],
                    university: [
                        {required: true, message: 'please enter University', trigger: 'blur'}
                    ],
                    qualification: [
                        {required: true, message: 'please choose qualification', trigger: 'blur'}
                    ],
                    subject: [
                        {required: true, message: 'please enter subject', trigger: 'blur'}
                    ],
                    year: [
                        {required: true, message: 'please choose your study year', trigger: 'blur'}
                    ],
                    expected: [
                        {required: true, message: 'please enter Expected Role', trigger: 'blur'}
                    ],
                    email: [
                        {required: true, message: 'Please enter your E-mail', trigger: 'blur'},
                        {type: 'email', message: 'Please enter your E-mail correctly', trigger: ['blur', 'change']}
                    ],
                    textarea: [
                        {required: true, message: 'Please introduce yourself,thank you', trigger: 'blur'}
                    ]
                }
            }
        },
        methods: {
            submitForm(formName) {
                for (let i = 0; i < this.expectedcheck.length; i++) {
                    this.postForm.expected = this.expectedcheck[i]+ ',' +this.postForm.expected
                }
                this.postForm.expected =  this.postForm.expected.substring(0, this.postForm.expected.length - 1);
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        let that = this
                        axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
                        axios.post('http://localhost:8081/send_mail', qs.stringify(this.postForm))
                            .then(function (res) {
                                if (res.data.status === 'success') {
                                    that.$alert('Applied Successfully!', 'Thank you!', {
                                        confirmButtonText: 'Confirm',
                                        callback: action => {
                                            that.$message({
                                                type: 'info',
                                                message: `action: ${action}`
                                            });
                                        }
                                    });
                                } else {
                                    that.$alert('Something Wrong Happened!', 'Sorry!', {
                                        confirmButtonText: 'Confirm',
                                        callback: action => {
                                            that.$message({
                                                type: 'info',
                                                message: `action: ${action}`
                                            });
                                        }
                                    });
                                }
                            })
                            .catch(function (error) {
                                that.$alert('Something Wrong Happened!', 'Sorry!', {
                                    confirmButtonText: 'Confirm',
                                    callback: action => {
                                        that.$message({
                                            type: 'info',
                                            message: `action: ${action}`
                                        });
                                    }
                                });
                            })


                    } else {
                        this.$alert('Something Wrong Happened!', 'Sorry!', {
                            confirmButtonText: 'Confirm',
                            callback: action => {
                                this.$message({
                                    type: 'info',
                                    message: `action: ${action}`
                                });
                            }
                        });
                    }
                });
            },
            resetForm(formName) {
                this.$refs[formName].resetFields();
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .dreams {
    padding: 10px 45px 20px 45px;
    background-color: #f2f2f2;
    border: 1px solid #ccc;
    box-shadow: 5px 3px 5px 5px grey;
  }

  h1 {
    font-weight: normal;
    text-align: center;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .postInfo-container-item {
    float: left;
  }

  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }

  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
  {
    opacity: 0;
  }
</style>
