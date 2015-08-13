(function () {

	angular.module('gueli.menu', ['ngAnimate'])
		.controller('MenuController', ['$scope', '$location', function($scope, $location) {

		    $scope.ShowSubMenuInv = function(valor) {
		    	$scope.SubMInventario = valor;
		    }

		}]);
})();
