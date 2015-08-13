(function (_) {

  angular.module('gueli.homepage', ['ngAnimate'])
    
    .factory('HomePageService', ['$http', '$q', '$filter', function ($http, $q, $filter) {

      function homepage() {
        return false;
      }

      return {
        homepage: homepage
      };

    }])

    //****************************************************
    //                                                   *
    //CONTROLLERS                                        *
    //                                                   *
    //****************************************************
    .controller('HomePageCtrl', ['$scope', '$filter', 'HomePageService', function ($scope, $filter, HomePageService) {


    }]);

})(_);