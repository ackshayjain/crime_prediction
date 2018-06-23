
var mysql = require('mysql');
var dbconfig = {
    host: 'mlab.com',
    user: 'devanshjain98',
    password: 'meddelivery',
    database: 'scotch'
};


function getTodos(callback) {

    var connection = mysql.createConnection(dbconfig);
    console.log("sqldb connected");
    connection.connect();
    connection.query('SELECT * FROM scotch where queryBody = JSONparseSQL(mlab.queryBody)',function (error,rows,fields) {
        if(error)
            throw error;
        callback(rows);


    });



}
var queryCtrl = angular.module('queryCtrl', ['geolocation', 'gservice']);
queryCtrl.controller('queryCtrl', function($scope, $log, $http, $rootScope, geolocation, gservice){

    // Initializes Variables
    // ----------------------------------------------------------------------------
    $scope.formData = {};
    var queryBody = {};

    // Functions
    // ----------------------------------------------------------------------------

    // Get User's actual coordinates based on HTML5 at window load
    geolocation.getLocation().then(function(data){
        coords = {lat:data.coords.latitude, long:data.coords.longitude};

        // Set the latitude and longitude equal to the HTML5 coordinates
        $scope.formData.longitude = parseFloat(coords.long).toFixed(3);
        $scope.formData.latitude = parseFloat(coords.lat).toFixed(3);
    });

    // Get coordinates based on mouse click. When a click event is detected....
    $rootScope.$on("clicked", function(){

        // Run the gservice functions associated with identifying coordinates
        $scope.$apply(function(){
            $scope.formData.latitude = parseFloat(gservice.clickLat).toFixed(3);
            $scope.formData.longitude = parseFloat(gservice.clickLong).toFixed(3);
        });
    });

    // Take query parameters and incorporate into a JSON queryBody
    $scope.queryUsers = function(){

        // Assemble Query Body
        queryBody = {
            longitude: parseFloat($scope.formData.longitude),
            latitude: parseFloat($scope.formData.latitude),
            distance: parseFloat($scope.formData.distance),
            crimetype: $scope.formData.crimetype,

            other: $scope.formData.other,
            minhoursago: $scope.formData.minhoursago,
            maxhoursago: $scope.formData.maxhoursago,
            Area: $scope.formData.Area,
            reqVerified: $scope.formData.verified
        };

        // Post the queryBody to the /query POST route to retrieve the filtered results
        $http.post('/query', queryBody)

        // Store the filtered results in queryResults
            .success(function(queryResults){

                var connection = mysql.createConnection(dbconfig);
                console.log("sqldb connected");
                connection.connect();

                if (error)
                    throw error;
                console.log("updated:"+id);


                // Pass the filtered results to the Google Map Service and refresh the map
                gservice.refresh(queryBody.latitude, queryBody.longitude, queryResults);

                // Count the number of records retrieved for the panel-footer
                $scope.queryCount = queryResults.length;

                function maxdistance(data, queryBody) {

                    ("SELECT *"
                        "FROM Crime c natural join Location l natural join Time as t"
                    "WHERE c.location.lat<=location.queryBody.lat+queryBody.distance.lat and" +
                    "c.location.lat<=location.queryBody.lat-queryBody.distance.lat" +
                        "c.location.lng<=location.queryBody.lng+queryBody.distance.lng" +
                        "c.location.lng<=location.queryBody.lng-queryBody.distance.lng")



                }


            })
            .error(function(queryResults){
                console.log('Error ' + queryResults);
            })
    };
});

