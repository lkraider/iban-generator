var ibaGeneratorModule = angular.module('iban-generator', []);

ibaGeneratorModule.config(function($routeProvider) {
  $routeProvider.
  when('/make', {
    controller: MakeCtrl,
    templateUrl: 'partials/make.html'
  }).
  when('/check', {
    controller: CheckCtrl,
    templateUrl: 'partials/check.html'
  }).
  otherwise({
    redirectTo: '/make'
  });
});

function MakeCtrl($scope, $http) {
  $scope.$parent.menu = 'make';
  $scope.banks = [];

  $('#ispbModal').on('hidden', function() {
    $('#makeButton').focus();
  });

  $http.get('rest/').success(function(data) {
    _.each(data.ispb, function(value, key, list) {
      var bank = {
        name: key,
        ispb: value
      };
      $scope.banks.push(bank);
    });
  });

  var onResult = function(data) {
    var iban = data.iban;
    if (iban === undefined) {
      iban = 'Error';
    }
    $scope.result = iban;
  };

  $scope.makeIban = function() {
    var url = 'rest/?agency=' + $scope.agency + '&account=' + $scope.account + '&ispb=' + $scope.ispb;
    $http.get(url).success(onResult).error(onResult);
  };

  $scope.selectIspb = function(ispb) {
    $scope.ispb = ispb;
  };
}

function CheckCtrl($scope, $http) {
  $scope.$parent.menu = 'check';
  $scope.result = null;

  var onResult = function(data) {
    var isValid = data.valid;
    if (isValid === undefined) {
      isValid = false;
    }
    $scope.result = {
      iban: $scope.iban,
      isValid: isValid
    };
  };

  $scope.checkIban = function() {
    var url = 'rest/?iban=' + $scope.iban;
    $http.get(url).success(onResult).error(onResult);
  };
}
