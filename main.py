<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unequal Grid Layout</title>
    <!-- Bootstrap 5 CSS CDN -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .box {
            padding: 20px;
            background-color: #f0f0f0;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
    </style>
</head>
<body class="bg-light">

    <div class="container my-5">
        <div class="row">
            <!-- First column (takes up 8 of 12 columns) -->
            <div class="col-md-8">
                <div class="box">
                    <h3>Column 1 (8/12)</h3>
                    <p>This column takes up 8 parts of the grid, making it larger.</p>
                </div>
            </div>

            <!-- Second column (takes up 4 of 12 columns) -->
            <div class="col-md-4">
                <div class="box">
                    <h3>Column 2 (4/12)</h3>
                    <p>This column takes up 4 parts of the grid, making it smaller than the first column.</p>
                </div>
            </div>
        </div>

        <div class="row mt-4">
            <!-- Third column (takes up 6 of 12 columns) -->
            <div class="col-md-6">
                <div class="box">
                    <h3>Column 3 (6/12)</h3>
                    <p>This column takes up 6 parts of the grid.</p>
                </div>
            </div>

            <!-- Fourth column (takes up 6 of 12 columns) -->
            <div class="col-md-6">
                <div class="box">
                    <h3>Column 4 (6/12)</h3>
                    <p>This column also takes up 6 parts of the grid.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Bootstrap 5 JS and dependencies (CDN) -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"></script>
</body>
</html>
