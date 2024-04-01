; Auto-generated. Do not edit!


(cl:in-package assignments-srv)


;//! \htmlinclude MapFilePath-request.msg.html

(cl:defclass <MapFilePath-request> (roslisp-msg-protocol:ros-message)
  ((map_file_path
    :reader map_file_path
    :initarg :map_file_path
    :type cl:string
    :initform ""))
)

(cl:defclass MapFilePath-request (<MapFilePath-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MapFilePath-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MapFilePath-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name assignments-srv:<MapFilePath-request> is deprecated: use assignments-srv:MapFilePath-request instead.")))

(cl:ensure-generic-function 'map_file_path-val :lambda-list '(m))
(cl:defmethod map_file_path-val ((m <MapFilePath-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader assignments-srv:map_file_path-val is deprecated.  Use assignments-srv:map_file_path instead.")
  (map_file_path m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MapFilePath-request>) ostream)
  "Serializes a message object of type '<MapFilePath-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'map_file_path))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'map_file_path))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MapFilePath-request>) istream)
  "Deserializes a message object of type '<MapFilePath-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'map_file_path) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'map_file_path) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MapFilePath-request>)))
  "Returns string type for a service object of type '<MapFilePath-request>"
  "assignments/MapFilePathRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MapFilePath-request)))
  "Returns string type for a service object of type 'MapFilePath-request"
  "assignments/MapFilePathRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MapFilePath-request>)))
  "Returns md5sum for a message object of type '<MapFilePath-request>"
  "fad351900b5fbe0dbdabf42eace39648")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MapFilePath-request)))
  "Returns md5sum for a message object of type 'MapFilePath-request"
  "fad351900b5fbe0dbdabf42eace39648")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MapFilePath-request>)))
  "Returns full string definition for message of type '<MapFilePath-request>"
  (cl:format cl:nil "string map_file_path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MapFilePath-request)))
  "Returns full string definition for message of type 'MapFilePath-request"
  (cl:format cl:nil "string map_file_path~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MapFilePath-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'map_file_path))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MapFilePath-request>))
  "Converts a ROS message object to a list"
  (cl:list 'MapFilePath-request
    (cl:cons ':map_file_path (map_file_path msg))
))
;//! \htmlinclude MapFilePath-response.msg.html

(cl:defclass <MapFilePath-response> (roslisp-msg-protocol:ros-message)
  ((success
    :reader success
    :initarg :success
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass MapFilePath-response (<MapFilePath-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <MapFilePath-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'MapFilePath-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name assignments-srv:<MapFilePath-response> is deprecated: use assignments-srv:MapFilePath-response instead.")))

(cl:ensure-generic-function 'success-val :lambda-list '(m))
(cl:defmethod success-val ((m <MapFilePath-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader assignments-srv:success-val is deprecated.  Use assignments-srv:success instead.")
  (success m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <MapFilePath-response>) ostream)
  "Serializes a message object of type '<MapFilePath-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'success) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <MapFilePath-response>) istream)
  "Deserializes a message object of type '<MapFilePath-response>"
    (cl:setf (cl:slot-value msg 'success) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<MapFilePath-response>)))
  "Returns string type for a service object of type '<MapFilePath-response>"
  "assignments/MapFilePathResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MapFilePath-response)))
  "Returns string type for a service object of type 'MapFilePath-response"
  "assignments/MapFilePathResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<MapFilePath-response>)))
  "Returns md5sum for a message object of type '<MapFilePath-response>"
  "fad351900b5fbe0dbdabf42eace39648")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'MapFilePath-response)))
  "Returns md5sum for a message object of type 'MapFilePath-response"
  "fad351900b5fbe0dbdabf42eace39648")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<MapFilePath-response>)))
  "Returns full string definition for message of type '<MapFilePath-response>"
  (cl:format cl:nil "bool success~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'MapFilePath-response)))
  "Returns full string definition for message of type 'MapFilePath-response"
  (cl:format cl:nil "bool success~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <MapFilePath-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <MapFilePath-response>))
  "Converts a ROS message object to a list"
  (cl:list 'MapFilePath-response
    (cl:cons ':success (success msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'MapFilePath)))
  'MapFilePath-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'MapFilePath)))
  'MapFilePath-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'MapFilePath)))
  "Returns string type for a service object of type '<MapFilePath>"
  "assignments/MapFilePath")