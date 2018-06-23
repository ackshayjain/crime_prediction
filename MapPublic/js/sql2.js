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
    connection.query('SELECT * FROM Crime',function (error,rows,fields) {
        if(error)
            throw error;
        callback(rows);


    });


function addData(){
    var connection = mysql.createConnection(dbconfig);
    console.log("sqldb connected");
    connection.connect();

    if (error)
        throw error;
    console.log("updated:"+id);


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


    connection.id.insert into "Crime" values (queryBody.details, queryBody.crimetype, queryBody.hoursago , queryBody.Area, queryBody.latitude, queryBody.longitude, queryBody.verified, queryBody.created_at);

    connection.id.insert into "Time" values (queryBody.details, queryBody.hoursago , queryBody.created_at);

    connection.id.insert into "Crime" values ( queryBody.Area, queryBody.latitude, queryBody.longitude)l;

}
}