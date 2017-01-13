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
          /*
            INITIAL FUNCTION THAT TRIGGERS WHEN PAGE LOADS
            FETCHES THE APPOINTMENTS FROM DRCHRONO API
            AND APP DB FOR DOCTOR DETAILS AND AVERAGE WAITING TIME
          */
        function init() {
            $scope.ob = {};
            $scope.appUrl = "/doctor/appointment/"
            $http.get($scope.appUrl).then(
                    function(response) {
                        $scope.appointments = response['data']['response'];
                        $scope.datawaiting = false;

                    })
                .catch(function(response) {
                    console.error('Gists error', response.status, response.data);
                });
                // FUNCTION TO OBTAIN DATA FROM APP DB
            $http.get('/detail/doctor').then(
                    function(response) {
                        $scope.doc_details = response['data'];
                        var wait_time = $scope.doc_details['total_wait_time'];
                        var total_patients = $scope.doc_details['total_patients'];
                        var temp = wait_time / total_patients;
                        $scope.mins = Math.floor(temp);
                        var temp2 = temp - $scope.mins;
                        if (temp2 == 0) {
                            $scope.secs = 0;
                        } else {
                            $scope.secs = Math.floor(temp2 * 60);
                        }
                    })
                .catch(function(response) {
                    console.error('Gists error', response.status, response.data);
                });
        }
        init();
        // MAIN FUNCTION TO PATCH DATA TO DRCHRONO API DATA
        function postDataToBackend(url, params, callback) {
            $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
            var params = $.param(params);
            $http.post(url, params)
                .then(callback);
        }
        // WRAPPER FUNCTION TO SET AN APPOINTMENT TO 'TO SESSION'
        $scope.setAppointmenttoSession = function(appid) {
            var url = "/doctor/appointment/";
            var params = {
                'appointment_id': appid,
                'status': 'In Session'
            };

            postDataToBackend(url, params, function() {
                init();
            });
        };
        // WRAPPER FUNCTION TO SET AN APPOINTMENT TO 'COMPLETED'
        $scope.setAppointmenttoCompleted = function(appid) {
            var url = "/doctor/appointment/";
            var params = {
                'appointment_id': appid,
                'status': 'Complete'
            };

            postDataToBackend(url, params, function() {
                alert("Done!");
                init();
            });
        };
        // FUNCTION TO OBATAIN THE WAITING TIME FOR EACH CHECKED IN PATIENT
        $scope.findDetails = function(app_id) {
            var url = '/detail/appointment/' + app_id;
            $http.get(url).then(function(response) {
                var date1 = new Date().getTime();

                var date2 = response['data']['time_of_arrival'];
                var date2 = new Date(response['data']['time_of_arrival']).getTime();
                var d3 = date1 - date2;
                var minDifference = Math.floor(d3 / 1000 / 60);
                for (var i = 0, l = $scope.appointments.length; i < l; i++) {
                    if ($scope.appointments[i]['id'] == app_id) {
                        $scope.appointments[i]['time'] = minDifference;
                    }
                }

            });
        };


    }]);
})();
