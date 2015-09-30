var addrBook = angular.module('addrBook', ['ngAnimate']);
 
addrBook.controller('AddrBook', function ($scope, $http) {

    $scope.changesCounter = 0;
    
    $http.get('MM.txt').success(function(data) {

        console.log(data);
        
        
    });
});