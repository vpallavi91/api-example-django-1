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
      $scope.mess = "pallavi"; 

    }]);
})();
