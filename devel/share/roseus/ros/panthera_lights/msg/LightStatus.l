;; Auto-generated. Do not edit!


(when (boundp 'panthera_lights::LightStatus)
  (if (not (find-package "PANTHERA_LIGHTS"))
    (make-package "PANTHERA_LIGHTS"))
  (shadow 'LightStatus (find-package "PANTHERA_LIGHTS")))
(unless (find-package "PANTHERA_LIGHTS::LIGHTSTATUS")
  (make-package "PANTHERA_LIGHTS::LIGHTSTATUS"))

(in-package "ROS")
;;//! \htmlinclude LightStatus.msg.html


(defclass panthera_lights::LightStatus
  :super ros::object
  :slots (_Brake _HazardLight _SignalRight _SignalLeft _Autonomous _TeleOp _Beacon _Night _Day ))

(defmethod panthera_lights::LightStatus
  (:init
   (&key
    ((:Brake __Brake) 0)
    ((:HazardLight __HazardLight) 0)
    ((:SignalRight __SignalRight) 0)
    ((:SignalLeft __SignalLeft) 0)
    ((:Autonomous __Autonomous) 0)
    ((:TeleOp __TeleOp) 0)
    ((:Beacon __Beacon) 0)
    ((:Night __Night) 0)
    ((:Day __Day) 0)
    )
   (send-super :init)
   (setq _Brake (round __Brake))
   (setq _HazardLight (round __HazardLight))
   (setq _SignalRight (round __SignalRight))
   (setq _SignalLeft (round __SignalLeft))
   (setq _Autonomous (round __Autonomous))
   (setq _TeleOp (round __TeleOp))
   (setq _Beacon (round __Beacon))
   (setq _Night (round __Night))
   (setq _Day (round __Day))
   self)
  (:Brake
   (&optional __Brake)
   (if __Brake (setq _Brake __Brake)) _Brake)
  (:HazardLight
   (&optional __HazardLight)
   (if __HazardLight (setq _HazardLight __HazardLight)) _HazardLight)
  (:SignalRight
   (&optional __SignalRight)
   (if __SignalRight (setq _SignalRight __SignalRight)) _SignalRight)
  (:SignalLeft
   (&optional __SignalLeft)
   (if __SignalLeft (setq _SignalLeft __SignalLeft)) _SignalLeft)
  (:Autonomous
   (&optional __Autonomous)
   (if __Autonomous (setq _Autonomous __Autonomous)) _Autonomous)
  (:TeleOp
   (&optional __TeleOp)
   (if __TeleOp (setq _TeleOp __TeleOp)) _TeleOp)
  (:Beacon
   (&optional __Beacon)
   (if __Beacon (setq _Beacon __Beacon)) _Beacon)
  (:Night
   (&optional __Night)
   (if __Night (setq _Night __Night)) _Night)
  (:Day
   (&optional __Day)
   (if __Day (setq _Day __Day)) _Day)
  (:serialization-length
   ()
   (+
    ;; uint8 _Brake
    1
    ;; uint8 _HazardLight
    1
    ;; uint8 _SignalRight
    1
    ;; uint8 _SignalLeft
    1
    ;; uint8 _Autonomous
    1
    ;; uint8 _TeleOp
    1
    ;; uint8 _Beacon
    1
    ;; uint8 _Night
    1
    ;; uint8 _Day
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _Brake
       (write-byte _Brake s)
     ;; uint8 _HazardLight
       (write-byte _HazardLight s)
     ;; uint8 _SignalRight
       (write-byte _SignalRight s)
     ;; uint8 _SignalLeft
       (write-byte _SignalLeft s)
     ;; uint8 _Autonomous
       (write-byte _Autonomous s)
     ;; uint8 _TeleOp
       (write-byte _TeleOp s)
     ;; uint8 _Beacon
       (write-byte _Beacon s)
     ;; uint8 _Night
       (write-byte _Night s)
     ;; uint8 _Day
       (write-byte _Day s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _Brake
     (setq _Brake (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _HazardLight
     (setq _HazardLight (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _SignalRight
     (setq _SignalRight (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _SignalLeft
     (setq _SignalLeft (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _Autonomous
     (setq _Autonomous (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _TeleOp
     (setq _TeleOp (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _Beacon
     (setq _Beacon (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _Night
     (setq _Night (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _Day
     (setq _Day (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get panthera_lights::LightStatus :md5sum-) "e88e78a8e709ed3fa5e5e18d48c62d5d")
(setf (get panthera_lights::LightStatus :datatype-) "panthera_lights/LightStatus")
(setf (get panthera_lights::LightStatus :definition-)
      "uint8 Brake
uint8 HazardLight
uint8 SignalRight
uint8 SignalLeft
uint8 Autonomous
uint8 TeleOp
uint8 Beacon
uint8 Night
uint8 Day

")



(provide :panthera_lights/LightStatus "e88e78a8e709ed3fa5e5e18d48c62d5d")


