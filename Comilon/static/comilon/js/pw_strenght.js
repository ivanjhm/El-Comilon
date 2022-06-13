$(document).ready(function() {
	var password1 		= $('#password1'); //id of first password field
	var password2		= $('#password2'); //id of second password field
	var passwordsInfo 	= $('#pass-info'); //id of indicator element
	
	passwordStrengthCheck(password1,password2,passwordsInfo); //call password check function
	
});

function passwordStrengthCheck(password1, password2, passwordsInfo)
{
	//Must contain 5 characters or more
	var WeakPass = /(?=.{5,}).*/; 
	//Must contain lower case letters and at least one digit.
	var MediumPass = /^(?=\S*?[a-z])(?=\S*?[0-9])\S{5,}$/; 
	//Must contain at least one upper case letter, one lower case letter and one digit.
	var StrongPass = /^(?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9])\S{5,}$/; 
	//Must contain at least one upper case letter, one lower case letter and one digit.
	var VryStrongPass = /^(?=\S*?[A-Z])(?=\S*?[a-z])(?=\S*?[0-9])(?=\S*?[^\w\*])\S{5,}$/; 
	
	$(password1).on('keyup', function(e) {
		if(VryStrongPass.test(password1.val()))
		{
			passwordsInfo.removeClass().addClass('vrystrongpass').html("¡Muy segura! (Impresionante, ¡no olvides tu pase ahora!)");
		}	
		else if(StrongPass.test(password1.val()))
		{
			passwordsInfo.removeClass().addClass('strongpass').html("Segura! (Ingrese caracteres especiales para hacerlo aún más segura)");
		}	
		else if(MediumPass.test(password1.val()))
		{
			passwordsInfo.removeClass().addClass('goodpass').html("Bien! (Ingrese letra mayúscula para hacer segura)");
		}
		else if(WeakPass.test(password1.val()))
    	{
			passwordsInfo.removeClass().addClass('stillweakpass').html("¡Aun debil! (Ingrese dígitos para hacer una buena contraseña)");
    	}
		else
		{
			passwordsInfo.removeClass().addClass('weakpass').html("¡Muy débil! (Debe tener 5 o más caracteres)");
		}
	});
	
	$(password2).on('keyup', function(e) {
		
		if(password1.val() !== password2.val())
		{
			passwordsInfo.removeClass().addClass('weakpass').html("¡Las contraseñas no coinciden!");	
		}else{
			passwordsInfo.removeClass().addClass('goodpass').html("¡Las contraseñas coinciden!");	
		}
			
	});
}