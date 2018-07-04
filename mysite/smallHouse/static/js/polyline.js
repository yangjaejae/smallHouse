function getPathLine(){

    var polyline = new naver.maps.Polyline({
        map: map,
        path: [],
        strokeColor: '#5347AA',
        strokeWeight: 2
    });
    naver.maps.Event.addListener(map, 'click', function(e) {
        var point = e.coord;
        var path = polyline.getPath();
        path.push(point);
        new naver.maps.Marker({
            map: map,
            position: point
        });
    });
}