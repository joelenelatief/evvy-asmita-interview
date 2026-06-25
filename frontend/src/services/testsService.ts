import { AxiosError, AxiosResponse } from "axios";
import { getRequest } from "../utils/axios";

const fetchTestResults = async ({
  isPositive,
  onSuccess,
  onFailure,
}: {
  isPositive?: boolean;
  onSuccess?: any;
  onFailure?: any;
}) => {
  const response = await getRequest(
    `/api/v1/test-results?is_positive=${isPositive}`,
    (response: AxiosResponse) => {
      if (onSuccess) { onSuccess(response.data); }
      return response;
    },
    (error: AxiosError) => {
      if (onFailure) { onFailure(error); }
      throw error;
    }
  );
  return response;
};

export const testsService = {
  fetchTestResults,
};
