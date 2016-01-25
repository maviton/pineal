(alias triangle
       (polygon 3
                :
                fill   (color 0 0 0 0)
                stroke (color 0 1 1)
                line   0.02
                radius 0.5))

(alias g1
       (polygon 4
                :
                fill     (color 0 1 1 0)
                rotation (/ pi 4)
                position [0.1 0.05]
                radius   0.5)
       (polygon 3
                :
                radius 0.2
                fill   (color 0 1 1 0.5)
                stroke (color 0 0 1))
       (triangle))


(layer render
       (group (g1 1)
              (g1 0.8)
              (g1 0.7)
              (triangle)
              :
              line   0.03
              fill   (color 1)
              stroke (color 0 1 0)
              rotate (/ pi 6)))


(window master   (render))
(window overwiew (render))
