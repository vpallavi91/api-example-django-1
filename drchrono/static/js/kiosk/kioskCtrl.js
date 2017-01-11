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
        $scope.patientDataWaiting = false;
        // This function is to retrieve data from the backend
        function getDatafromBackend(url, params, callback) {
            $http.get(url, {
                    params: params
                })
                .then(callback)
								.catch(function(response) {
  							console.error('Gists error', response.status, response.data);
								$scope.err = true;
								$scope.patientDataWaiting = false;

							});
        }
				function postDataToBackend(url, params, callback) {
					$http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
					var params = $.param(params);
					alert(params);
					$http.post(url, params)
                .then(callback);
        }
        // This is the caller function to retrieve patient data from the backend
        $scope.pat = function() {
						if ($scope.first_name==undefined || $scope.last_name==undefined || $scope.dob==undefined)
						{

								$scope.validationerror =true;
						}
						else {
							$scope.patientDataWaiting = true;
	            $scope.patientData = false;
							$scope.paterr = false;
							$scope.validationerror =false;
							alert($scope.first_name,$scope.last_name,$scope.dob);
							$scope.patUrl = "/kiosk/patient/"
	            $http.get($scope.patUrl, {
								params:{
	                    "f_name": $scope.first_name,
	                    "l_name": $scope.last_name,
	                    "dob": $scope.dob
	                }}).then(
	                function(response) {
											$scope.paterr = false;
											$scope.validationerror =false;
	                    $scope.patient = response['data'];
	                    $scope.id = $scope.patient['id'];
	                    $scope.patientData = true;
	                })
									.catch(function(response) {
	  							console.error('Gists error', response.status, response.data);
									$scope.paterr = true;
									$scope.validationerror =false;
									$scope.patientDataWaiting = false;

								});
						}
        };
        // This is the caller function to retrieve patient data from the backend

        //Reset the form fields
        $scope.reset = function() {
            $scope.patientDataWaiting = false;
            $scope.patientData = false;
            getDatafromBackend("/kiosk/appointment/", {
                    "p_id": $scope.id
                },
                function(response) {
                    $scope.appointment = response['data'];
										$scope.time1 = $scope.appointment['scheduled_time'];
										$scope.time = $scope.time1.substring(11);
										$scope.duration = $scope.appointment['duration'];
										$scope.appointment_id = $scope.appointment['id'];
										alert($scope.appointment_id);
                });
        };

				 $scope.setAppointmenttoArrived = function() {
					 alert("inside post function");
					var url = "/kiosk/appointment/";
					var params = {'appointment_id': $scope.appointment_id,
								  'status': 'Arrived'};

					postDataToBackend(url, params, function () {
							alert("success");
					});
				};

    }]);
})();
