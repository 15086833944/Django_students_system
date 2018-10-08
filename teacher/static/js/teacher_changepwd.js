
// function chechname(){
// 			if($("#name").val().length>=6 && $("#name").val().length<=18){
// 				$("#uname").html("通过");
// 				return true
// 			}else{
// 				$("#uname").html("必须是6-18位");
// 				return false
// 			}
// 		};

		function checkpwd1(){
			if($("#pwd1").val().length>=6){
				$("#upwd1").html("通过");
				return true
			}else{
				$("#upwd1").html("必须是6位以上");
				return false
			}
		};

		function checkpwd2(){
			if($("#pwd2").val()==$("#pwd1").val() && $("#pwd2").val()!=""){
				$("#upwd2").html("通过");
				return true
			}else{
				$("#upwd2").html("必须与密码一致");
				return false
			}
		};

		// $("#name").blur(chechname);
		$("#pwd1").blur(checkpwd1);
		$("#pwd2").blur(checkpwd2);

		$("form").submit(function(){
			return checkpwd1() && checkpwd2()
		});