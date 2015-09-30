var fs       = require('fs'),
    encoding = 'utf8';

function write (path, data) {

    fs.open(path, "w", 0644, function(err, file) {
    
        if (!err) {

            fs.write(file, JSON.stringify(data), null, encoding, function(err, written) {
                    
                if (err) {
                
                    console.log(WRITE_FAIL);
                
                }

                fs.close(file);

            });

        }

    });

}

function qsort (arr, prop) {

    if (arr.length <= 1) return arr;
    if (arr.length == 2) {

        if (arr[0][prop] < arr[1][prop]) return [arr[1], arr[0]]
        else return arr;
    }

    var h = [], l = [], m = [arr[0]], m0 = m[0][prop];

    for (var i = 1; i < arr.length; i++) {

        if (arr[i][prop] > m0) h.push(arr[i])
        else {

            if (arr[i][prop] == m0) m.push(arr[i])
            else l.push(arr[i])
        }
    }

    return qsort(h, prop).concat(m).concat( qsort(l, prop) );
}

function getObj (arr) {

    var o = {}, arrObjs = [];

    for (var a = 0; a < arr.length; a++) {

        o[ arr[a] ] = o[ arr[a] ] + 1 || 1;
    }

    for (a in o) {

        arrObjs.push({
            name : a,
            data : o[a]
        });
    }

    arrObjs = qsort(arrObjs, 'data');

    for (var i = 0; i < arrObjs.length; i++) {

        arrObjs[i].cypf = arrObjs[i].data * (i + 1);
    }

    console.log('length: ', arr.length);

    return arrObjs;
}

function pureArr (data) {

    return data.toLowerCase().replace(/ –/g, " ").replace(/- /g, " ").replace(/[«»\.,:–;\'\"\?!]/g, '').replace(/\s+/g, ' ').split(' ');
}

function stat (pathname, callback) {

    fs.lstat(pathname, function(err, s) {

        if (!err) {

            fs.open(pathname, 'r', 0644, function(err, file) {

                if (err) {

                    return;

                } else {

                    fs.read(file, s.size, null, encoding, function(err, data) {

                        fs.close(file);
                        // console.log(pureArr(data));

                        var retD = getObj( pureArr(data) );
                        write('out.txt', retD);
                        callback(retD);

                    })

                }

            });

        }

    });
}

// stat('/pride.txt');
// stat('MM.txt');
exports.stat = stat;