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
      function postDataToBackend(url, params, callback) {
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        var params = $.param(params);
        alert(params);
        $http.post(url, params)
              .then(callback);
      }

      $scope.setAppointmenttoSession = function(appid) {
        alert("inside post function");
       var url = "/doctor/appointment/";
       var params = {'appointment_id': appid,
               'status': 'In Session'};

       postDataToBackend(url, params, function () {
           alert("success");
       });
     };
     $scope.setAppointmenttoCompleted = function(appid) {
       alert("inside post function");
      var url = "/doctor/appointment/";
      var params = {'appointment_id': appid,
              'status': 'Complete'};

      postDataToBackend(url, params, function () {
          alert("success");
      });
    };
    }]);
})();
