webpackJsonp([1],{NHnr:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var r=a("7+uW"),o={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]};var s=a("VU/8")({name:"App"},o,!1,function(e){a("yIPq")},null,null).exports,l=a("zL8q"),i=a.n(l),n=a("wUZ8"),c=a.n(n),p=(a("tvR6"),a("/ocq")),m=a("mtWM"),u=a.n(m),f=a("mw3O"),d=a.n(f),v={name:"HelloWorld",data:function(){return{msg:"Welcome to DreamsAI",postForm:{lastname:"",firstname:"",university:"",qualification:"",subject:"",year:"",expected:"",email:"",textarea:""},expectedlist:["{ML} Model Researcher","{ML} Model/ Software Developer","Firefighting Coder","Front End Developer","Data Scientist","Knowledge Engineer","System Architect","DevOps Architect"],expectedcheck:[],radio:"1",rules:{lastname:[{required:!0,message:"please enter Last Name",trigger:"blur"}],firstname:[{required:!0,message:"please enter First Name",trigger:"blur"}],university:[{required:!0,message:"please enter University",trigger:"blur"}],qualification:[{required:!0,message:"please choose qualification",trigger:"blur"}],subject:[{required:!0,message:"please enter subject",trigger:"blur"}],year:[{required:!0,message:"please choose your study year",trigger:"blur"}],expected:[{required:!0,message:"please enter Expected Role",trigger:"blur"}],email:[{required:!0,message:"Please enter your E-mail",trigger:"blur"},{type:"email",message:"Please enter your E-mail correctly",trigger:["blur","change"]}],textarea:[{required:!0,message:"Please introduce yourself,thank you",trigger:"blur"}]}}},methods:{submitForm:function(e){for(var t=this,a=0;a<this.expectedcheck.length;a++)this.postForm.expected=this.expectedcheck[a]+","+this.postForm.expected;this.postForm.expected=this.postForm.expected.substring(0,this.postForm.expected.length-1),this.$refs[e].validate(function(e){if(e){var a=t;u.a.defaults.headers.post["Content-Type"]="application/x-www-form-urlencoded",u.a.post("/send_mail",d.a.stringify(t.postForm)).then(function(e){"success"===e.data.status?a.$alert("Applied Successfully!","Thank you!",{confirmButtonText:"Confirm",callback:function(e){a.$message({type:"info",message:"action: "+e})}}):a.$alert("Something Wrong Happened!","Sorry!",{confirmButtonText:"Confirm",callback:function(e){a.$message({type:"info",message:"action: "+e})}})}).catch(function(e){a.$alert("Something Wrong Happened!","Sorry!",{confirmButtonText:"Confirm",callback:function(e){a.$message({type:"info",message:"action: "+e})}})})}else t.$alert("Something Wrong Happened!","Sorry!",{confirmButtonText:"Confirm",callback:function(e){t.$message({type:"info",message:"action: "+e})}})})},resetForm:function(e){this.$refs[e].resetFields()}}},b={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"dreams"},[a("h1",[e._v(e._s(e.msg))]),e._v(" "),a("el-form",{ref:"postForm",staticClass:"form-container",attrs:{model:e.postForm,"label-width":"150px",rules:e.rules,"label-position":"left"}},[a("el-row",[a("el-col",{attrs:{span:12}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"First Name",prop:"firstname"}},[a("el-input",{staticStyle:{width:"200px"},model:{value:e.postForm.firstname,callback:function(t){e.$set(e.postForm,"firstname",t)},expression:"postForm.firstname"}})],1)],1),e._v(" "),a("el-col",{attrs:{span:12}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"Last Name",prop:"lastname"}},[a("el-input",{staticStyle:{width:"200px"},model:{value:e.postForm.lastname,callback:function(t){e.$set(e.postForm,"lastname",t)},expression:"postForm.lastname"}})],1)],1)],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:12}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"University",prop:"university"}},[a("el-input",{staticStyle:{width:"350px"},model:{value:e.postForm.university,callback:function(t){e.$set(e.postForm,"university",t)},expression:"postForm.university"}})],1)],1),e._v(" "),a("el-col",{attrs:{span:12}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"Qualification",prop:"qualification"}},[a("el-select",{staticStyle:{width:"200px"},model:{value:e.postForm.qualification,callback:function(t){e.$set(e.postForm,"qualification",t)},expression:"postForm.qualification"}},[a("el-option",{attrs:{label:"Bachelor",value:"Bachelor"}}),e._v(" "),a("el-option",{attrs:{label:"Master",value:"Master"}}),e._v(" "),a("el-option",{attrs:{label:"Phd",value:"Phd"}}),e._v(" "),a("el-option",{attrs:{label:"Others",value:"Others"}})],1)],1)],1)],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:24}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"Subject",prop:"subject"}},[a("el-input",{staticStyle:{width:"350px"},model:{value:e.postForm.subject,callback:function(t){e.$set(e.postForm,"subject",t)},expression:"postForm.subject"}})],1)],1)],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:24}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"Year of Study",prop:"year"}},[a("el-select",{attrs:{placeholder:"please select your year"},model:{value:e.postForm.year,callback:function(t){e.$set(e.postForm,"year",t)},expression:"postForm.year"}},[a("el-option",{attrs:{label:"Year 1",value:"year1"}}),e._v(" "),a("el-option",{attrs:{label:"Year 2",value:"year2"}}),e._v(" "),a("el-option",{attrs:{label:"Year 3",value:"year3"}}),e._v(" "),a("el-option",{attrs:{label:"Year 4",value:"year4"}})],1)],1)],1)],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:24}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"Preferred Role",prop:"expected"}},[a("el-checkbox-group",{model:{value:e.expectedcheck,callback:function(t){e.expectedcheck=t},expression:"expectedcheck"}},e._l(e.expectedlist,function(e){return a("el-checkbox",{key:e,attrs:{label:e}})}),1)],1)],1)],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:24}},[a("el-form-item",{staticClass:"postInfo-container-item",attrs:{label:"E-mail",prop:"email"}},[a("el-input",{staticStyle:{width:"400px"},model:{value:e.postForm.email,callback:function(t){e.$set(e.postForm,"email",t)},expression:"postForm.email"}})],1)],1)],1),e._v(" "),a("el-row",[a("el-col",{attrs:{span:24}},[a("el-form-item",{attrs:{prop:"textarea",label:"A little bit about yourself"}},[a("el-input",{attrs:{type:"textarea",autosize:{minRows:5,maxRows:20},placeholder:"Please type something about you here",maxlength:"1000","show-word-limit":""},model:{value:e.postForm.textarea,callback:function(t){e.$set(e.postForm,"textarea",t)},expression:"postForm.textarea"}})],1)],1)],1),e._v(" "),a("el-form-item",{staticStyle:{"text-align":"center","margin-top":"20px"}},[a("el-button",{attrs:{type:"primary"},on:{click:function(t){return e.submitForm("postForm")}}},[e._v("Submit")]),e._v(" "),a("el-button",{on:{click:function(t){return e.resetForm("postForm")}}},[e._v("Reset")])],1)],1)],1)},staticRenderFns:[]};var g=a("VU/8")(v,b,!1,function(e){a("vyJV")},"data-v-0a526dcf",null).exports;r.default.use(p.a);var y=new p.a({routes:[{path:"/",name:"Dreams",component:g}]});r.default.config.productionTip=!1,r.default.use(i.a,{locale:c.a}),new r.default({el:"#app",router:y,components:{App:s},template:"<App/>"})},tvR6:function(e,t){},vyJV:function(e,t){},yIPq:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.291036da9a19a74b6715.js.map