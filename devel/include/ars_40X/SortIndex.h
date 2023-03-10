// Generated by gencpp from file ars_40X/SortIndex.msg
// DO NOT EDIT!


#ifndef ARS_40X_MESSAGE_SORTINDEX_H
#define ARS_40X_MESSAGE_SORTINDEX_H

#include <ros/service_traits.h>


#include <ars_40X/SortIndexRequest.h>
#include <ars_40X/SortIndexResponse.h>


namespace ars_40X
{

struct SortIndex
{

typedef SortIndexRequest Request;
typedef SortIndexResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SortIndex
} // namespace ars_40X


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ars_40X::SortIndex > {
  static const char* value()
  {
    return "93fb6a7e64dbd2a0708217b8ad8f0eb8";
  }

  static const char* value(const ::ars_40X::SortIndex&) { return value(); }
};

template<>
struct DataType< ::ars_40X::SortIndex > {
  static const char* value()
  {
    return "ars_40X/SortIndex";
  }

  static const char* value(const ::ars_40X::SortIndex&) { return value(); }
};


// service_traits::MD5Sum< ::ars_40X::SortIndexRequest> should match
// service_traits::MD5Sum< ::ars_40X::SortIndex >
template<>
struct MD5Sum< ::ars_40X::SortIndexRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ars_40X::SortIndex >::value();
  }
  static const char* value(const ::ars_40X::SortIndexRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ars_40X::SortIndexRequest> should match
// service_traits::DataType< ::ars_40X::SortIndex >
template<>
struct DataType< ::ars_40X::SortIndexRequest>
{
  static const char* value()
  {
    return DataType< ::ars_40X::SortIndex >::value();
  }
  static const char* value(const ::ars_40X::SortIndexRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ars_40X::SortIndexResponse> should match
// service_traits::MD5Sum< ::ars_40X::SortIndex >
template<>
struct MD5Sum< ::ars_40X::SortIndexResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ars_40X::SortIndex >::value();
  }
  static const char* value(const ::ars_40X::SortIndexResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ars_40X::SortIndexResponse> should match
// service_traits::DataType< ::ars_40X::SortIndex >
template<>
struct DataType< ::ars_40X::SortIndexResponse>
{
  static const char* value()
  {
    return DataType< ::ars_40X::SortIndex >::value();
  }
  static const char* value(const ::ars_40X::SortIndexResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ARS_40X_MESSAGE_SORTINDEX_H
