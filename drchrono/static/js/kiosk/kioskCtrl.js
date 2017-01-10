(function() {
    var app = angular.module("kiosk", []);
    app.config(['$httpProvider',
        function($httpProvider) {
            $httpProvider.defaults.xsrfCookieName = 'csrftoken';
            $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
            $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        }
    ]);
    app.controller('kioskCtrl', ['$scope', '$http', function($scope, $http) {
        $scope.message = "pallavi";

        function getEndpoint(url, params, callback) {
            $http.get(url, {
                    params: params
                })
                .then(callback);
        }
				$scope.pat = function(){
        getEndpoint("/kiosk/patient/", {
                "f_name": $scope.first_name,
								"l_name": $scope.last_name,
								"dob":$scope.dob
            },
            function(response) {
                $scope.patients = response['data'];
								alert($scope.patients);
            });
					};

    }]);
})();
