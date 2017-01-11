(function() {
    var app = angular.module("doctor", []);
    app.config(['$httpProvider',
        function($httpProvider) {
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        }
    ]);
    app.controller('doctorCtrl', ['$scope', '$http', function($scope, $http) {
      $scope.datawaiting = true;
      function init(){
        $scope.mess = "pallavi";
        $scope.appUrl = "/doctor/appointment/"
        $http.get($scope.appUrl ).then(
            function(response) {

                $scope.appointments = response['data']['response'];
                $scope.datawaiting = false;
            })
            .catch(function(response) {
            console.error('Gists error', response.status, response.data);


          });
      }
      init();

    }]);
})();
