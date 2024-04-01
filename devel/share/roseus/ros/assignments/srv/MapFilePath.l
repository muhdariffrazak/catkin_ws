;; Auto-generated. Do not edit!


(when (boundp 'assignments::MapFilePath)
  (if (not (find-package "ASSIGNMENTS"))
    (make-package "ASSIGNMENTS"))
  (shadow 'MapFilePath (find-package "ASSIGNMENTS")))
(unless (find-package "ASSIGNMENTS::MAPFILEPATH")
  (make-package "ASSIGNMENTS::MAPFILEPATH"))
(unless (find-package "ASSIGNMENTS::MAPFILEPATHREQUEST")
  (make-package "ASSIGNMENTS::MAPFILEPATHREQUEST"))
(unless (find-package "ASSIGNMENTS::MAPFILEPATHRESPONSE")
  (make-package "ASSIGNMENTS::MAPFILEPATHRESPONSE"))

(in-package "ROS")





(defclass assignments::MapFilePathRequest
  :super ros::object
  :slots (_map_file_path ))

(defmethod assignments::MapFilePathRequest
  (:init
   (&key
    ((:map_file_path __map_file_path) "")
    )
   (send-super :init)
   (setq _map_file_path (string __map_file_path))
   self)
  (:map_file_path
   (&optional __map_file_path)
   (if __map_file_path (setq _map_file_path __map_file_path)) _map_file_path)
  (:serialization-length
   ()
   (+
    ;; string _map_file_path
    4 (length _map_file_path)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _map_file_path
       (write-long (length _map_file_path) s) (princ _map_file_path s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _map_file_path
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _map_file_path (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass assignments::MapFilePathResponse
  :super ros::object
  :slots (_success ))

(defmethod assignments::MapFilePathResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass assignments::MapFilePath
  :super ros::object
  :slots ())

(setf (get assignments::MapFilePath :md5sum-) "fad351900b5fbe0dbdabf42eace39648")
(setf (get assignments::MapFilePath :datatype-) "assignments/MapFilePath")
(setf (get assignments::MapFilePath :request) assignments::MapFilePathRequest)
(setf (get assignments::MapFilePath :response) assignments::MapFilePathResponse)

(defmethod assignments::MapFilePathRequest
  (:response () (instance assignments::MapFilePathResponse :init)))

(setf (get assignments::MapFilePathRequest :md5sum-) "fad351900b5fbe0dbdabf42eace39648")
(setf (get assignments::MapFilePathRequest :datatype-) "assignments/MapFilePathRequest")
(setf (get assignments::MapFilePathRequest :definition-)
      "string map_file_path
---
bool success


")

(setf (get assignments::MapFilePathResponse :md5sum-) "fad351900b5fbe0dbdabf42eace39648")
(setf (get assignments::MapFilePathResponse :datatype-) "assignments/MapFilePathResponse")
(setf (get assignments::MapFilePathResponse :definition-)
      "string map_file_path
---
bool success


")



(provide :assignments/MapFilePath "fad351900b5fbe0dbdabf42eace39648")


