; Auto-generated. Do not edit!


(cl:in-package panthera_lights-msg)


;//! \htmlinclude LightStatus.msg.html

(cl:defclass <LightStatus> (roslisp-msg-protocol:ros-message)
  ((Brake
    :reader Brake
    :initarg :Brake
    :type cl:fixnum
    :initform 0)
   (HazardLight
    :reader HazardLight
    :initarg :HazardLight
    :type cl:fixnum
    :initform 0)
   (SignalRight
    :reader SignalRight
    :initarg :SignalRight
    :type cl:fixnum
    :initform 0)
   (SignalLeft
    :reader SignalLeft
    :initarg :SignalLeft
    :type cl:fixnum
    :initform 0)
   (Autonomous
    :reader Autonomous
    :initarg :Autonomous
    :type cl:fixnum
    :initform 0)
   (TeleOp
    :reader TeleOp
    :initarg :TeleOp
    :type cl:fixnum
    :initform 0)
   (Beacon
    :reader Beacon
    :initarg :Beacon
    :type cl:fixnum
    :initform 0)
   (Night
    :reader Night
    :initarg :Night
    :type cl:fixnum
    :initform 0)
   (Day
    :reader Day
    :initarg :Day
    :type cl:fixnum
    :initform 0))
)

(cl:defclass LightStatus (<LightStatus>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <LightStatus>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'LightStatus)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name panthera_lights-msg:<LightStatus> is deprecated: use panthera_lights-msg:LightStatus instead.")))

(cl:ensure-generic-function 'Brake-val :lambda-list '(m))
(cl:defmethod Brake-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:Brake-val is deprecated.  Use panthera_lights-msg:Brake instead.")
  (Brake m))

(cl:ensure-generic-function 'HazardLight-val :lambda-list '(m))
(cl:defmethod HazardLight-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:HazardLight-val is deprecated.  Use panthera_lights-msg:HazardLight instead.")
  (HazardLight m))

(cl:ensure-generic-function 'SignalRight-val :lambda-list '(m))
(cl:defmethod SignalRight-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:SignalRight-val is deprecated.  Use panthera_lights-msg:SignalRight instead.")
  (SignalRight m))

(cl:ensure-generic-function 'SignalLeft-val :lambda-list '(m))
(cl:defmethod SignalLeft-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:SignalLeft-val is deprecated.  Use panthera_lights-msg:SignalLeft instead.")
  (SignalLeft m))

(cl:ensure-generic-function 'Autonomous-val :lambda-list '(m))
(cl:defmethod Autonomous-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:Autonomous-val is deprecated.  Use panthera_lights-msg:Autonomous instead.")
  (Autonomous m))

(cl:ensure-generic-function 'TeleOp-val :lambda-list '(m))
(cl:defmethod TeleOp-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:TeleOp-val is deprecated.  Use panthera_lights-msg:TeleOp instead.")
  (TeleOp m))

(cl:ensure-generic-function 'Beacon-val :lambda-list '(m))
(cl:defmethod Beacon-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:Beacon-val is deprecated.  Use panthera_lights-msg:Beacon instead.")
  (Beacon m))

(cl:ensure-generic-function 'Night-val :lambda-list '(m))
(cl:defmethod Night-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:Night-val is deprecated.  Use panthera_lights-msg:Night instead.")
  (Night m))

(cl:ensure-generic-function 'Day-val :lambda-list '(m))
(cl:defmethod Day-val ((m <LightStatus>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader panthera_lights-msg:Day-val is deprecated.  Use panthera_lights-msg:Day instead.")
  (Day m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <LightStatus>) ostream)
  "Serializes a message object of type '<LightStatus>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Brake)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'HazardLight)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SignalRight)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SignalLeft)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Autonomous)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'TeleOp)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Beacon)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Night)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Day)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <LightStatus>) istream)
  "Deserializes a message object of type '<LightStatus>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Brake)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'HazardLight)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SignalRight)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'SignalLeft)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Autonomous)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'TeleOp)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Beacon)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Night)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'Day)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<LightStatus>)))
  "Returns string type for a message object of type '<LightStatus>"
  "panthera_lights/LightStatus")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'LightStatus)))
  "Returns string type for a message object of type 'LightStatus"
  "panthera_lights/LightStatus")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<LightStatus>)))
  "Returns md5sum for a message object of type '<LightStatus>"
  "e88e78a8e709ed3fa5e5e18d48c62d5d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'LightStatus)))
  "Returns md5sum for a message object of type 'LightStatus"
  "e88e78a8e709ed3fa5e5e18d48c62d5d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<LightStatus>)))
  "Returns full string definition for message of type '<LightStatus>"
  (cl:format cl:nil "uint8 Brake~%uint8 HazardLight~%uint8 SignalRight~%uint8 SignalLeft~%uint8 Autonomous~%uint8 TeleOp~%uint8 Beacon~%uint8 Night~%uint8 Day~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'LightStatus)))
  "Returns full string definition for message of type 'LightStatus"
  (cl:format cl:nil "uint8 Brake~%uint8 HazardLight~%uint8 SignalRight~%uint8 SignalLeft~%uint8 Autonomous~%uint8 TeleOp~%uint8 Beacon~%uint8 Night~%uint8 Day~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <LightStatus>))
  (cl:+ 0
     1
     1
     1
     1
     1
     1
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <LightStatus>))
  "Converts a ROS message object to a list"
  (cl:list 'LightStatus
    (cl:cons ':Brake (Brake msg))
    (cl:cons ':HazardLight (HazardLight msg))
    (cl:cons ':SignalRight (SignalRight msg))
    (cl:cons ':SignalLeft (SignalLeft msg))
    (cl:cons ':Autonomous (Autonomous msg))
    (cl:cons ':TeleOp (TeleOp msg))
    (cl:cons ':Beacon (Beacon msg))
    (cl:cons ':Night (Night msg))
    (cl:cons ':Day (Day msg))
))
