var login = angular.module("login-modulo", ['ui.bootstrap', "ngCookies"]);

login.run(function($http,$cookies){$http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;})
.config(function($interpolateProvider) {$interpolateProvider.startSymbol('{$');$interpolateProvider.endSymbol('$}');});

login.controller("formController", ["$http", "$sce", funciones]);

function funciones($http, $sce, $scope){
	var fcon = this;
	fcon.datos = {}

	fcon.enviar = function(){
		$http.post("validar-login", fcon.datos)
		.success(function(data){
				console.log(data);
		});
	}
}