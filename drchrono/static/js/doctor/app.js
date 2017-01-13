(function() {
    var app = angular.module("app", ['smart-table']);

    app.controller('MainCtrl', ['$scope', '$http', function($scope, $http) {



        var vm = this;

        // Declare the array for the selected items
        vm.selected = [];

        // Function to get data for all selected items
        vm.selectAll = function(collection) {

            // if there are no items in the 'selected' array,
            // push all elements to 'selected'
            if (vm.selected.length === 0) {

                angular.forEach(collection, function(val) {

                    vm.selected.push(val.app_id);

                });

                // if there are items in the 'selected' array,
                // add only those that ar not
            } else if (vm.selected.length > 0 && vm.selected.length != vm.data.length) {

                angular.forEach(collection, function(val) {

                    var found = vm.selected.indexOf(val.id);

                    if (found == -1) vm.selected.push(val.id);

                });

                // Otherwise, remove all items
            } else {

                vm.selected = [];

            }

        };

        // Function to get data by selecting a single row
        vm.select = function(id) {

            var found = vm.selected.indexOf(id);

            if (found == -1) vm.selected.push(id);

            else vm.selected.splice(found, 1);

        }


        var url = '/list/appointment/'
        $http.get(url).then(function(response) {
            vm.rowCollection = response.data;
        });
        //vm.rowCollection = [];



        vm.data = [].concat(vm.rowCollection);

        $scope.calAvg = function() {
            vm.sum = 0;
            vm.total = 0;
            vm.selected.forEach(function(el) {
                vm.data.forEach(function(at) {
                    if (el == at['app_id']) {
                        vm.sum += at['wait_time'];
                        vm.total++;
                    }
                });
            });
            vm.avg = vm.sum / vm.total;
        }
    }]);
})();
